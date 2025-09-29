from util.utility import Utility

class DirectCurrentCalculator:

    @staticmethod
    def dc_power_sub_menu(languageManager):
        print(f'*** {languageManager.get_word('dc_menu_power_title')} ***')
        print(f'\t{languageManager.get_word('dc_menu_power_math')}')

        result, voltage = Utility.parseFloat(input(f'{languageManager.get_word('dc_menu_p_input_v')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return

        result, amper = Utility.parseFloat(input(f'{languageManager.get_word('dc_menu_p_input_a')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
        
        power = voltage * amper
        print(f'{languageManager.get_word('dc_menu_power_result')}: {power:.2f} W')

    @staticmethod
    def dc_voltage_sub_menu(languageManager):
        print(f'*** {languageManager.get_word('dc_menu_voltage_title')} ***')
        print(f'\t{languageManager.get_word('dc_menu_voltage_math')}')

        result, amper = Utility.parseFloat(input(f'{languageManager.get_word('dc_menu_p_input_a')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
        
        result, resistence = Utility.parseFloat(input(f'{languageManager.get_word('dc_menu_input_ohms')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return

        print(f'{languageManager.get_word('dc_menu_voltage_result')}: {(resistence * amper):.2f} V')

    @staticmethod
    def dc_resistance_sub_menu(languageManager):
        print(f'*** {languageManager.get_word('dc_menu_resistance_title')} ***')
        print(f'\t{languageManager.get_word('dc_menu_resistance_math')}')

        result, voltage = Utility.parseFloat(input(f'{languageManager.get_word('dc_menu_p_input_v')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return

        result, amper = Utility.parseFloat(input(f'{languageManager.get_word('dc_menu_p_input_a')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return

        if amper <= 0.0:
            print(f'{languageManager.get_word('dc_menu_resistance_error_amper')}')
            return

        print(f'{languageManager.get_word('dc_menu_resistance_result')}: {(voltage / amper):.2f} Ω')

    @staticmethod
    def dc_amperios_sub_menu(languageManager):
        print(f'*** {languageManager.get_word('dc_menu_amperios_title')} ***')
        print(f'\t{languageManager.get_word('dc_menu_amperios_math')}')
        
        result, voltage = Utility.parseFloat(input(f'{languageManager.get_word('dc_menu_p_input_v')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return

        result, resistence = Utility.parseFloat(input(f'{languageManager.get_word('dc_menu_input_ohms')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return

        if resistence <= 0.0:
            print(f'{languageManager.get_word('dc_menu_resistance_error')}')
            return

        print(f'{languageManager.get_word('dc_menu_amperios_result')}: {(voltage / resistence):.2f} A')