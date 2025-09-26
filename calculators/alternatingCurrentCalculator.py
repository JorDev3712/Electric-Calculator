import math

from util.utility import Utility

class AlternaningCurrentCalculator:
    
    # It allows to know the phase system
    isThirdPhase = False

    # Calculates the apparent powere using the formula S = V x I
    @classmethod
    def dc_power_menu(cls, languageManager):
        print(f'*** {languageManager.get_word('power')} ***')
        print(f'\t{languageManager.get_word('ac_menu_power_math')}')

        result, voltage = Utility.parseFloat(input(f'{languageManager.get_word('ac_menu_power_input_01')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
        
        result, current = Utility.parseFloat(input(f'{languageManager.get_word('ac_menu_power_input_03')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
        
        power = voltage * current * (math.sqrt(3) if cls.isThirdPhase else 1)
        print(f'{languageManager.get_word('ac_menu_power_results')}: {power:.2f} VA ≈ {(power/1000):.2f} kVA')

    # Calculates the apparent power using the formula S = P x fp
    @classmethod
    def dc_power_menu_02(cls, languageManager):
        print(f'*** {languageManager.get_word('power')} ***')
        print(f'\t{languageManager.get_word('ac_menu_power_math')}')

        result, potence = Utility.parseFloat(input(f'{languageManager.get_word('ac_menu_power_input_01')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
        
        result, fp = Utility.parseFloat(input(f'{languageManager.get_word('ac_menu_power_input_02')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
        
        print(f'{languageManager.get_word('ac_menu_power_results')}: {(potence * fp):.2f} VA')

    
    @classmethod
    def dc_real_power_menu(cls, languageManager):
        print(f'*** {languageManager.get_word('real_power')} ***')
        print(f'\t{languageManager.get_word('ac_menu_r_power_math')}')

        result, voltage = Utility.parseFloat(input(f'{languageManager.get_word('ac_menu_power_input_01')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
        
        result, current = Utility.parseFloat(input(f'{languageManager.get_word('ac_menu_power_input_03')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
        
        result, fp = Utility.parseFloat(input(f'{languageManager.get_word('ac_menu_power_input_02')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
        
        power = voltage * current * fp * (math.sqrt(3) if cls.isThirdPhase else 1)
        print(f'{languageManager.get_word('ac_menu_r_power_results')}: {power:.2f} W ≈ {(power/1000):.2f} kW')

        