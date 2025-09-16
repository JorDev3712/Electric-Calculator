# Metodos

from calculators.peukert import MathPeukert

def execute(opt: int)->bool:
    exit = False
    if opt == 11:
        cal = MathPeukert()
        cal.showMenu()
    elif opt == 3:
        print('Closing...! Hasta pronto!')
        exit = True

    return exit
        

def showMenu()->int:
    print('*** Calculadora eléctrica ***')
    print('''Menu:
        1. Corriente alterna.
        2. Corriente continua.
        3. Salir''')
    return int(input('Escribe la opción: '))

def showSubMenuCA()->int:
    print('''Menu:
        1. Calcular potencia monofásica (kVA).
        2. Calcular potencia real monofásica (kW).
        3. Calcular potencia trifásica (kVA).
        4. Calcular potencia real trifásica (kW).
        5. Calcular potencia (CC).
        6. Calcular corriente alterna (A).
        7. Calcular tensión alterna (U).
        8. Calcular corriente continua.
        9. Calcular tensión continua.
        10. Calcular ohmeaje.
        11. Calcular autonomia de UPS.
        12. Salir''')
    return int(input('Escribe la opción: '))

def loop():
    exit = False
    while not exit:
        option = showMenu()
        exit = execute(option)

# Main code
if __name__ == '__main__':
    loop()
