class Language:
    def __init__(self, id, code, text):
        self.__id = id
        self.__code = code
        self.text = text

    def __str__(self):
        return self.text