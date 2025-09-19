from .controller import Controller

class LanguageController(Controller):
    def __init__(self, languageManager):
        self.__languageManager = languageManager
        self.__exit = False

    def execute(self, option:int)->bool:
        if option == 3:
            print(self.__languageManager.get_word('good_bye_text'))
            self.__exit = True
        return self.__exit

    def show_menu(self)->int:
        print(f'''{self.__languageManager.get_word('menu_language_title')}:
            1. {self.__languageManager.get_word('menu_language_option_1')}.
            2. {self.__languageManager.get_word('menu_language_option_2')}.
            3. {self.__languageManager.get_word('menu_exit')}.''')
        return int(input(self.__languageManager.get_word('menu_select_option')))
    
    def loop(self):
        pass
