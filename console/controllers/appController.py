from .controller import Controller

class AppController(Controller):
    _exit = False

    def __init__(self, languageManager):
        self.__languageManager = languageManager

    def loader(self):
        self.__languageManager.load()
    
    def execute(self, option:int)->bool:
        if option == 3:
            AppController._exit = True
            print('Closing.... See you soon!')
        return AppController._exit
    
    def show_menu(self)->int:
        print('''Choice a language:
            1. Español.
            2. English.
            3. Exit.''')
        return int(input('Option: '))

    def loop(self):
        while not AppController._exit:
            option = self.show_menu()
            AppController._exit = self.execute(option)