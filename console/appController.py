import controllers.Controller

class AppController(controllers.Controller):
    _exit = False

    def __init__(self):
        pass
    
    def execute(self)->bool:
        return AppController._exit
    
    def showMenu(self)->int:
        return 0

    def loop(self):
        while not AppController._exit:
            option = self.showMenu()
            AppController._exit = self.execute(option)