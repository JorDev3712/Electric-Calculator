# Online Python - IDE, Editor, Compiler, Interpreter

class MathPerkert:

    # Methods
    def calculate(self, a, c = 20):
        ref = (0.45 / a) ** 1.2
        hours = (ref * c)
        mins = hours * 60
        return ref, hours, mins
    
    def humanConsole(self, cal):
        (ref, hours, mins) = cal
        print(f'''Valores obtenidos:
        Iref: {ref:.3} A
        Horas: {hours:.3} h
        Minutos: ± {mins:.4} m''')
    
    def showMenu(self):
        print('*** Calcular el valor de Peukert ***')
        value = float(input('Ingresa el valor de la corriente total: '))
        pila = input('Valor de la bateria: ')
        bat = 20
        if pila != '':
            bat = float(pila)
        self.humanConsole(self.calculate(value, bat))
