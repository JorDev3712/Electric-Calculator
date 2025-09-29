import math

from util.utility import Utility

class AlternaningCurrentCalculator:
    
    # It allows to know the phase system
    isThirdPhase = False

    # Calculates the apparent powere using the formula S = V x I
    @classmethod
    def dc_power_menu(cls, languageManager):
        print(f'*** {languageManager.get_word('power')} ***')

        if cls.isThirdPhase:
            print(f'\t{languageManager.get_word('ac_menu_power_math_third')}')
        else:
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

        if cls.isThirdPhase:
            print(f'\t{languageManager.get_word('ac_menu_r_power_math_third')}')
        else:
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

    @classmethod
    def dc_voltage_menu(cls, languageManager):
        res = 'n'
        if cls.isThirdPhase:
            res = input(f'{languageManager.get_word('ac_menu_voltage_input_01')}: ')
            res = res.lower()

        if not "y" in res:
            print(f'*** {languageManager.get_word('voltage')} ***')
            print(f'\t{languageManager.get_word('ac_menu_voltage_math')}')
        else:
            print(f'*** {languageManager.get_word('voltage')} + {languageManager.get_word('neutral')} ***')
            print(f'\t{languageManager.get_word('ac_menu_voltage_math_third_02')}')
            print(f'\t{languageManager.get_word('ac_menu_voltage_math_third_01')}')
            
        result, power = Utility.parseFloat(input(f'{languageManager.get_word('ac_menu_power_input_04')}: '))
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
            
        voltage = power / (current * fp)
        if cls.isThirdPhase and "y" in res:
            voltage /= math.sqrt(3)

        print(f'{languageManager.get_word('ac_menu_voltage_results')}: {voltage:.2f} V')


    @classmethod
    def dc_amper_menu(cls, languageManager):
        # res = 'n'
        # if cls.isThirdPhase:
        #     res = input(f'{languageManager.get_word('ac_menu_voltage_input_01')}: ')
        #     res = res.lower()
        
        print(f'*** {languageManager.get_word('amper')} ***')
        print(f'\t{languageManager.get_word('ac_menu_current_math')}')
        # if not "y" in res:
            
        # else:
        #     print(f'\t{languageManager.get_word('ac_menu_amper_math_third_01')}')
        #     print(f'\t{languageManager.get_word('ac_menu_amper_math_third_02')}')
            
        result, power = Utility.parseFloat(input(f'{languageManager.get_word('ac_menu_power_input_04')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
            
        result, voltage = Utility.parseFloat(input(f'{languageManager.get_word('ac_menu_power_input_01')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
            
        result, fp = Utility.parseFloat(input(f'{languageManager.get_word('ac_menu_power_input_02')}: '))
        if not result:
            print(f'{languageManager.get_word('ac_menu_power_error_01')}')
            return
            
        current = power / (voltage * fp * (math.sqrt(3) if cls.isThirdPhase else 1))

        print(f'{languageManager.get_word('ac_menu_current_results')}: {current:.2f} A')