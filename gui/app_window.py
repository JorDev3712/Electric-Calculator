import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from components.switch import ModernSwitch

class ElectricCalculatorWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_window()
        self.config_style()
        self.config_grid()
        self.create_components()

    def config_window(self):
        # Sets size the window
        self.geometry('350x400')
        # No Resize the window
        self.resizable(0,0)
        # Changes the window color
        self.configure(background='#1d2d44')
        # Edits the title
        self.title('Calculadora para Electricista')

    def config_style(self):
        # We define a style
        self.estilos = ttk.Style()
        self.estilos.theme_use('clam') # Dark theme
        self.estilos.configure(self, background='#1d2d44',
                 foreground='white',
                 fieldbackground='black')
        self.estilos.configure('RedBorder.TFrame', background='#1d2d44',
                               bordercolor='red', borderwidth=3, relief='solid')
        self.estilos.configure('TButton', background='#3a86ff',
                               foreground='white',
                               font=('Arial', 18),
                               height=45, 
                               width=6)
        self.estilos.configure('TLabel', font=('Arial', 18))
        # Define event style
        self.estilos.map('TButton', background=[('hover', '#1d2d44')])

    def config_grid(self):
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.rowconfigure(2, weight=3)

    def create_components(self):
        title_label = ttk.Label(self, text='Calculadora para Electricista')
        title_label.grid(row=0, column=0, padx=15, pady=15, sticky=tk.NW)

        frame1 = ttk.Frame(self, style='RedBorder.TFrame')
        frame1.rowconfigure(0, weight=0)
        frame1.rowconfigure(1, weight=1)

        self.switch = ModernSwitch(frame1)

        self.result_label = ttk.Label(frame1, text='0')
        self.result_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NE)
        self.switch.grid(row=0, column=0, padx=10, sticky=tk.NW)

        frame1_sub = ttk.Frame(frame1, style='RedBorder.TFrame')
        frame1_sub.columnconfigure(0, weight=1)
        frame1_sub.columnconfigure(1, weight=1)
        frame1_sub.columnconfigure(2, weight=1)
        frame1_sub.columnconfigure(3, weight=1)
        frame1_sub.columnconfigure(4, weight=1)
        frame1_sub.rowconfigure(0, weight=1)
        frame1_sub.rowconfigure(1, weight=1)
        frame1_sub.rowconfigure(2, weight=1)

        self.button_one = ttk.Button(frame1_sub, text='1')
        self.button_one.grid(row=0, column=0, padx=5)
        
        self.button_two = ttk.Button(frame1_sub, text='2')
        self.button_two.grid(row=0, column=1, padx=5)
        
        self.button_third = ttk.Button(frame1_sub, text='3')
        self.button_third.grid(row=0, column=2, padx=5)
        
        self.button_four = ttk.Button(frame1_sub, text='4')
        self.button_four.grid(row=1, column=0, padx=5, pady=5)

        self.button_five = ttk.Button(frame1_sub, text='5')
        self.button_five.grid(row=1, column=1, padx=5, pady=5)

        self.button_six = ttk.Button(frame1_sub, text='6')
        self.button_six.grid(row=1, column=2, padx=5, pady=5)

        self.button_seven = ttk.Button(frame1_sub, text='7')
        self.button_seven.grid(row=2, column=0, padx=5)

        self.button_eight = ttk.Button(frame1_sub, text='8')
        self.button_eight.grid(row=2, column=1, padx=5)

        self.button_nine = ttk.Button(frame1_sub, text='9')
        self.button_nine.grid(row=2, column=2, padx=5)

        frame1_sub.grid(row=1, column=0, sticky='')
        frame1.grid(row=1, sticky=tk.NSEW)
        

# Main code
if __name__ == '__main__':
    app = ElectricCalculatorWindow()
    app.mainloop()    
