from util.utility import Utility

class AlternaningCurrentCalculator:
    
    # It allows to know the phase system
    isThirdPhase = False

    @classmethod
    def dc_power_menu(cls, languageManager):
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

        