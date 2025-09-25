# Online Python - IDE, Editor, Compiler, Interpreter

class PeukertCalculator:

    # Methods
    @classmethod
    def __calculate(cls, a, bat, bat_current, parallel):
        ref_current = bat_current / bat
        capacity = bat * parallel
        ref = (ref_current / a) ** 1.2
        hours = (ref * capacity)
        mins = hours * 60
        return ref, hours, mins
    
    @classmethod
    def __humanConsole(cls, cal, languageManager):
        (ref, hours, mins) = cal
        print(f'''{languageManager.get_word('dc_menu_peukert_results')}:
        Iref: {ref:.3} A
        Horas: {hours:.3} h
        Minutos: ± {mins:.4} m''')
    
    @classmethod
    def dc_sub_menu(cls, languageManager):
        print(f'*** {languageManager.get_word('dc_menu_peukert_title')} ***')
        total_current = float(input(f'{languageManager.get_word('dc_menu_peukert_input_01')}: '))
        bat = int(input(f'{languageManager.get_word('dc_menu_peukert_input_02')}: '))
        bat_hours = int(input(f'{languageManager.get_word('dc_menu_peukert_input_03')}: '))
        parallel_bat = int(input(f'{languageManager.get_word('dc_menu_peukert_input_04')}: '))
        cls.__humanConsole(cls.__calculate(total_current, bat, bat_hours, parallel_bat), languageManager)
