import tkinter as tk
import random

class IceCreamGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ice Cream Scoop Throwing Game")
        
        self.score = 0
        self.time_left = 30  
        
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="#f0f0f0")
        self.canvas.pack()
        
        self.target = self.canvas.create_oval(260, 330, 340, 410, fill="#ff4d4d", outline="")
        self.target_coords = self.canvas.coords(self.target)
        
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 14))
        self.score_label.pack()

        self.timer_label = tk.Label(self.root, text=f"Time Left: {self.time_left}s", font=("Arial", 14))
        self.timer_label.pack()
        
        self.throw_button = tk.Button(self.root, text="Throw Scoop", command=self.throw_ice_cream_scoop)
        self.throw_button.pack(pady=10)
        
        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=10)
        
        self.update_timer()
    
    def throw_ice_cream_scoop(self):
        start_x = random.randint(50, 550)
        scoop = self.canvas.create_oval(start_x-20, 360, start_x+20, 400, fill="#ffcc99", outline="")
        
        self.animate_scoop(scoop)
    
    def animate_scoop(self, scoop):
        x_velocity = random.uniform(-2, 2)
        y_velocity = -8
        
        def update():
            nonlocal x_velocity, y_velocity
            self.canvas.move(scoop, x_velocity, y_velocity)
            scoop_coords = self.canvas.coords(scoop)
            
            if scoop_coords[1] <= 0:
                y_velocity = 8  
            elif scoop_coords[3] >= 400:
                y_velocity = 0  
                self.check_hit(scoop)
                return
            
            y_velocity += 0.3  
            self.root.after(20, update)
        
        update()
    
    def check_hit(self, scoop):
        scoop_coords = self.canvas.coords(scoop)
        
        if (self.target_coords[0] <= scoop_coords[0] <= self.target_coords[2] and
            self.target_coords[1] <= scoop_coords[1] <= self.target_coords[3]):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        
        self.canvas.delete(scoop)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()
    
    def end_game(self):
        self.canvas.create_text(300, 200, text="Game Over!", font=("Arial", 24), fill="red")
        self.canvas.create_text(300, 240, text=f"Final Score: {self.score}", font=("Arial", 18), fill="black")

    def reset_game(self):
        self.score = 0
        self.time_left = 30
        self.score_label.config(text=f"Score: {self.score}")
        self.timer_label.config(text=f"Time Left: {self.time_left}s")
        self.canvas.delete("all")
        self.target = self.canvas.create_oval(260, 330, 340, 410, fill="#ff4d4d", outline="")
        self.target_coords = self.canvas.coords(self.target)
        self.update_timer()
        
if __name__ == "__main__":
    root = tk.Tk()
    game = IceCreamGame(root)
    root.mainloop()
