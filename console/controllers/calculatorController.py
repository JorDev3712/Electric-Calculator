from .controller import Controller

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
        self._isThirdPhase = False

    # This method will execute all the actions in the menus
    def execute(self, option:int)->bool:
        # Managements the AC and DC Menu
        if self._current_menu == 0:
            if option == 1:
                self._current_menu = 1
            elif option == 2:
                self._current_menu = 2
            elif option == 3:
                print(self.__languageManager.get_word('good_bye_text'))
                self.exit = self._mini_loop = True
            else:
                print(self.__languageManager.get_word('invalid_menu_select_option'))
        elif self._current_menu == 1:
            if option == 1:
                self._isThirdPhase = False
                self._current_menu = 3
            if option == 2:
                self._isThirdPhase = True
                self._current_menu = 3
            elif option == 3:
                self._current_menu = 0
            else:
                print(self.__languageManager.get_word('invalid_menu_select_option'))
        elif self._current_menu == 2:
            if option == 6:
                print(self.__languageManager.get_word('good_bye_text'))
                self.exit = self._mini_loop = True
        elif self._current_menu == 3:
            if option == 6:
                print(self.__languageManager.get_word('good_bye_text'))
                self.exit = self._mini_loop = True
        return self._mini_loop
    
    # It allows to choose a sub menu between DC or AC
    def show_menu(self)->int:
        if self._current_menu == 0:
            print(f'*** {self.__languageManager.get_word('title')} ***')
            print(f'''{self.__languageManager.get_word('menu_title')}
                1. {self.__languageManager.get_word('menu_opt_1')}.
                2. {self.__languageManager.get_word('menu_opt_2')}.
                3. {self.__languageManager.get_word('menu_exit')}''')
        elif self._current_menu == 1:
            self.show_sub_menu()
        elif self._current_menu == 2:
            self.show_menu_dc()
        elif self._current_menu == 3:
            self.show_menu_ac()
        return int(input(f'{self.__languageManager.get_word('menu_select_option')}'))
    
    # Displays the fase menu between one fase or third fase
    def show_sub_menu(self)->int:
        print(f'''{self.__languageManager.get_word('menu_title')}
            1. {self.__languageManager.get_word('sub_1_menu_opt_1')}
            2. {self.__languageManager.get_word('sub_1_menu_opt_2')}
            3. {self.__languageManager.get_word('menu_back')}
            4. {self.__languageManager.get_word('menu_exit')}''')

    # Displays the alternating current menu
    def show_menu_ac(self)->int:
        print(f'''{self.__languageManager.get_word('menu_title')} {self.__languageManager.get_word('sub_1_menu_opt_1' if self._isThirdPhase else 'sub_1_menu_opt_2')}
            1. {self.__languageManager.get_word('power')}
            2. {self.__languageManager.get_word('real_power')}
            3. {self.__languageManager.get_word('voltage')}
            4. {self.__languageManager.get_word('amper')}
            5. {self.__languageManager.get_word('menu_back')}
            6. {self.__languageManager.get_word('menu_exit')}''')

    # Displays the direct current menu
    def show_menu_dc(self)->int:
        print(f'''{self.__languageManager.get_word('menu_title')}
            1. {self.__languageManager.get_word('power')}
            2. {self.__languageManager.get_word('real_power')}
            3. {self.__languageManager.get_word('voltage')}
            4. {self.__languageManager.get_word('amper')}
            5. {self.__languageManager.get_word('menu_back')}
            6. {self.__languageManager.get_word('menu_exit')}''')

    def loop(self):
        while not self._mini_loop:
            option = self.show_menu()
            self._mini_loop = self.execute(option)