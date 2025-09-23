from .controller import Controller

class LanguageController(Controller):
    def __init__(self, languageManager):
        self.__languageManager = languageManager
        self._mini_loop = False
        self.exit = False

    def execute(self, option:int)->bool:
        self._mini_loop = True
        if option == 1:
            self.__languageManager.set_current_language('es')
        elif option == 2:
            self.__languageManager.set_current_language('en')
        elif option == 3:
            print(self.__languageManager.get_word('good_bye_text'))
            self.exit = True
        else:
            print(self.__languageManager.get_word('invalid_menu_select_option'))
            self._mini_loop = False
        return self._mini_loop

    def show_menu(self)->int:
        print(f'''{self.__languageManager.get_word('menu_language_title')}
            1. {self.__languageManager.get_word('menu_language_option_1')}.
            2. {self.__languageManager.get_word('menu_language_option_2')}.
            3. {self.__languageManager.get_word('menu_exit')}.''')
        return int(input(self.__languageManager.get_word('menu_select_option')))
    
    def loop(self):
        while not self._mini_loop:
            option = self.show_menu()
            self._mini_loop = self.execute(option)
