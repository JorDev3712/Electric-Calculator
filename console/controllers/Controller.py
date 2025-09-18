from abc import ABC, abstractmethod

class Controller(ABC):

    @abstractmethod
    def execute(self, option: int)->bool:
        pass

    @abstractmethod
    def show_menu(self)->int:
        pass