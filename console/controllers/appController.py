from .controller import Controller
from .languageController import LanguageController
from .calculatorController import CalculatorController

class AppController(Controller):
    _exit = False

    def __init__(self, languageManager):
        self.__languageManager = languageManager
        self.controllers = [
            LanguageController(self.__languageManager),
            CalculatorController(self.__languageManager)
        ]

    def loader(self):
        self.__languageManager.load()
    
    def execute(self, option:int)->bool:
        pass
    
    def show_menu(self)->int:
        pass

    def loop(self):
        index = 0
        while not AppController._exit:
            if index >= len(self.controllers):
                AppController._exit = True
                break
            self.controllers[index].loop()
            AppController._exit = self.controllers[index].exit
            index += 1