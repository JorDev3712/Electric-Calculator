from .controller import Controller
from calculators.directCurrentCalculator import DirectCurrentCalculator
from calculators.alternatingCurrentCalculator import AlternaningCurrentCalculator
from calculators.peukertCalculator import PeukertCalculator

from util.utility import Utility

class CalculatorController(Controller):
    def __init__(self, languageManager):
        self.__languageManager = languageManager
        
        # It allows to close the internal loop
        self._mini_loop = False

        # It allows to close the app
        self.exit = False

        # It allows to know the current menu to be displayed
        self._current_menu = 0

        # It allows to know the phase system
        AlternaningCurrentCalculator.isThirdPhase = False

    # This method will execute all the actions in the menus
    def execute(self, option:int)->bool:
        # Managements the AC and DC Menu
        if self._current_menu == 0:
            if option == 1:
                self._current_menu = 1
            elif option == 2:
                self._current_menu = 2
            elif option == 3:
                self.close()
            else:
                print(self.__languageManager.get_word('invalid_menu_select_option'))
        # Managements the phase menu
        elif self._current_menu == 1:
            if option == 1:
                AlternaningCurrentCalculator.isThirdPhase = False
                self._current_menu = 3
            if option == 2:
                AlternaningCurrentCalculator.isThirdPhase = True
                self._current_menu = 3
            elif option == 3:
                self._current_menu = 0
            elif option == 4:
                self.close()
            else:
                print(self.__languageManager.get_word('invalid_menu_select_option'))
        # Managements the DC menu
        elif self._current_menu == 2:
            if option == 1:
                DirectCurrentCalculator.dc_power_sub_menu(self.__languageManager)
            elif option == 2:
                DirectCurrentCalculator.dc_voltage_sub_menu(self.__languageManager)
            elif option == 3:
                DirectCurrentCalculator.dc_resistance_sub_menu(self.__languageManager)
            elif option == 4:
                DirectCurrentCalculator.dc_amperios_sub_menu(self.__languageManager)
            elif option == 4:
                DirectCurrentCalculator.dc_amperios_sub_menu(self.__languageManager)
            elif option == 5:
                PeukertCalculator.dc_sub_menu(self.__languageManager)
            elif option == 6:
                self._current_menu = 0
            elif option == 7:
                self.close()
            else:
                print(self.__languageManager.get_word('invalid_menu_select_option'))
        # Managements the AC menu
        elif self._current_menu == 3:
            if option == 1:
                AlternaningCurrentCalculator.dc_power_menu(self.__languageManager)
            elif option == 2:
                AlternaningCurrentCalculator.dc_real_power_menu(self.__languageManager)
            elif option == 3:
                AlternaningCurrentCalculator.dc_voltage_menu(self.__languageManager)
            elif option == 4:
                AlternaningCurrentCalculator.dc_amper_menu(self.__languageManager)
            elif option == 5:
                self._current_menu = 1
            elif option == 6:
                self.close()
        return self._mini_loop
    
    # It allows to choose a sub menu between DC or AC
    def show_menu(self)->int:
        if self._current_menu == 0:
            print(f'*** {self.__languageManager.get_word('title')} ***')
            print(f'''{self.__languageManager.get_word('menu_title')}:
                1. {self.__languageManager.get_word('menu_opt_1')}.
                2. {self.__languageManager.get_word('menu_opt_2')}.
                3. {self.__languageManager.get_word('menu_exit')}''')
        elif self._current_menu == 1:
            self.show_sub_menu()
        elif self._current_menu == 2:
            self.show_menu_dc()
        elif self._current_menu == 3:
            self.show_menu_ac()

        result, option = Utility.parseInt(input(f'{self.__languageManager.get_word('menu_select_option')}: '))
        if not result:
            print(self.__languageManager.get_word('invalid_menu_select_option'))
            option = -1
        
        return option
    
    # Displays the phase menu between one fase or third fase
    def show_sub_menu(self)->int:
        print(f'''{self.__languageManager.get_word('menu_title')} - {self.__languageManager.get_word('menu_opt_1')}
            1. {self.__languageManager.get_word('sub_1_menu_opt_1')}
            2. {self.__languageManager.get_word('sub_1_menu_opt_2')}
            3. {self.__languageManager.get_word('menu_back')}
            4. {self.__languageManager.get_word('menu_exit')}''')

    # Displays the alternating current menu
    def show_menu_ac(self)->int:
        print(f'''{self.__languageManager.get_word('menu_title')} - {self.__languageManager.get_word('menu_opt_1')} - {self.__languageManager.get_word('sub_1_menu_opt_2' if AlternaningCurrentCalculator.isThirdPhase else 'sub_1_menu_opt_1')}
            1. {self.__languageManager.get_word('power')}
            2. {self.__languageManager.get_word('real_power')}
            3. {self.__languageManager.get_word('voltage')}
            4. {self.__languageManager.get_word('amper')}
            5. {self.__languageManager.get_word('menu_back')}
            6. {self.__languageManager.get_word('menu_exit')}''')

    # Displays the direct current menu
    def show_menu_dc(self)->int:
        print(f'''{self.__languageManager.get_word('menu_title')} - {self.__languageManager.get_word('menu_opt_2')}
            1. {self.__languageManager.get_word('real_power')}
            2. {self.__languageManager.get_word('voltage')}
            3. {self.__languageManager.get_word('resistance')}
            4. {self.__languageManager.get_word('amper')}
            5. {self.__languageManager.get_word('batery_peukert')}
            6. {self.__languageManager.get_word('menu_back')}
            7. {self.__languageManager.get_word('menu_exit')}''')
        
    def close(self):
        print(self.__languageManager.get_word('good_bye_text'))
        self.exit = self._mini_loop = True

    def loop(self):
        while not self._mini_loop:
            option = self.show_menu()
            self._mini_loop = self.execute(option)