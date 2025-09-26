class DirectCurrentCalculator:

    @staticmethod
    def dc_power_sub_menu(languageManager):
        print(f'*** {languageManager.get_word('dc_menu_power_title')} ***')
        print(f'\t{languageManager.get_word('dc_menu_power_math')}')
        voltage = float(input(f'{languageManager.get_word('dc_menu_p_input_v')}: '))
        amper = float(input(f'{languageManager.get_word('dc_menu_p_input_a')}: '))
        print(f'{languageManager.get_word('dc_menu_power_result')}: {(voltage * amper):.2f} W')

    @staticmethod
    def dc_voltage_sub_menu(languageManager):
        print(f'*** {languageManager.get_word('dc_menu_voltage_title')} ***')
        print(f'\t{languageManager.get_word('dc_menu_voltage_math')}')
        amper = float(input(f'{languageManager.get_word('dc_menu_p_input_a')}: '))
        resistence = float(input(f'{languageManager.get_word('dc_menu_input_ohms')}: '))
        print(f'{languageManager.get_word('dc_menu_voltage_result')}: {(resistence * amper):.2f} V')

    @staticmethod
    def dc_resistance_sub_menu(languageManager):
        print(f'*** {languageManager.get_word('dc_menu_resistance_title')} ***')
        print(f'\t{languageManager.get_word('dc_menu_resistance_math')}')
        voltage = float(input(f'{languageManager.get_word('dc_menu_p_input_v')}: '))
        amper = float(input(f'{languageManager.get_word('dc_menu_p_input_a')}: '))

        if amper <= 0.0:
            print(f'{languageManager.get_word('dc_menu_resistance_error_amper')}')
            return

        print(f'{languageManager.get_word('dc_menu_resistance_result')}: {(voltage / amper):.2f} Ω')

    @staticmethod
    def dc_amperios_sub_menu(languageManager):
        print(f'*** {languageManager.get_word('dc_menu_amperios_title')} ***')
        print(f'\t{languageManager.get_word('dc_menu_amperios_math')}')
        voltage = float(input(f'{languageManager.get_word('dc_menu_p_input_v')}: '))
        resistence = float(input(f'{languageManager.get_word('dc_menu_input_ohms')}: '))

        if resistence <= 0.0:
            print(f'{languageManager.get_word('dc_menu_resistance_error')}')
            return

        print(f'{languageManager.get_word('dc_menu_amperios_result')}: {(voltage / resistence):.2f} A')