from abc import ABC, abstractmethod

class Controller(ABC):

    @abstractmethod
    def execute()->bool:
        pass

    @abstractmethod
    def showMenu():
        pass