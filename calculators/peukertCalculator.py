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
        {languageManager.get_word('dc_menu_peukert_h_01')}: {hours:.3} h
        {languageManager.get_word('dc_menu_peukert_h_02')}: ± {mins:.4} m''')
    
    @classmethod
    def dc_sub_menu(cls, languageManager):
        bats = [5,10,15,20,30,40,50,60,70,80,100]
        print(f'*** {languageManager.get_word('dc_menu_peukert_title')} ***')
        total_current = float(input(f'{languageManager.get_word('dc_menu_peukert_input_01')}: '))
        bat = int(input(f'{languageManager.get_word('dc_menu_peukert_input_02')}: '))
        if not bat in bats:
            print(f'{languageManager.get_word('dc_menu_peukert_bat_error')}')
            return
        bat_hours = int(input(f'{languageManager.get_word('dc_menu_peukert_input_03')}: '))
        parallel_bat = int(input(f'{languageManager.get_word('dc_menu_peukert_input_04')}: '))
        cls.__humanConsole(cls.__calculate(total_current, bat, bat_hours, parallel_bat), languageManager)
