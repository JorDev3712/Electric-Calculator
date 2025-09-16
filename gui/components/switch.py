import tkinter as tk

class ModernSwitch(tk.Canvas):
    def __init__(self, master=None, width=60, height=30, bg_color="#d5d5d5", active_color="#4cd137", knob_color="white", animation_steps=5, command=None, **kwargs):
        super().__init__(master, width=width, height=height, highlightthickness=0, bg=master["bg"], **kwargs)

        self.width = width
        self.height = height
        self.radius = height // 2
        self.bg_color = bg_color
        self.active_color = active_color
        self.knob_color = knob_color
        self.animation_steps = animation_steps
        self.command = command

        self.switch_on = False
        self.knob_pos = self.radius  # posición inicial del centro del knob

        self.track = self.create_round_rect(0, 0, width, height, radius=self.radius, fill=self.bg_color)
        self.knob = self.create_oval(2, 2, height - 2, height - 2, fill=self.knob_color, outline="")

        self.bind("<Button-1>", self.toggle)

    def create_round_rect(self, x1, y1, x2, y2, radius=25, **kwargs):
        points = [
            x1+radius, y1,
            x2-radius, y1,
            x2, y1,
            x2, y1+radius,
            x2, y2-radius,
            x2, y2,
            x2-radius, y2,
            x1+radius, y2,
            x1, y2,
            x1, y2-radius,
            x1, y1+radius,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def toggle(self, event=None):
        self.switch_on = not self.switch_on
        self.animate()
        if self.command:
            self.command(self.switch_on)

    def animate(self, step=0):
        start = self.coords(self.knob)[0]
        end = self.width - self.height + 2 if self.switch_on else 2
        delta = (end - start) / self.animation_steps

        if step < self.animation_steps:
            self.move(self.knob, delta, 0)
            self.after(10, lambda: self.animate(step + 1))
        else:
            final_fill = self.active_color if self.switch_on else self.bg_color
            self.itemconfig(self.track, fill=final_fill)

    def get(self):
        return self.switch_on

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Switch Moderno")
    root.geometry("200x100")
    root.configure(bg="#f0f0f0")

    def estado_switch(estado):
        print("Switch activado:" if estado else "Switch desactivado")

    switch = ModernSwitch(root, command=estado_switch)
    switch.pack(pady=20)

    root.mainloop()
