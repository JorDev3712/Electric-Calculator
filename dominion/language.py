class Language:
    def __init__(self, code: str, text: str):
        self.__code = code
        self.text = text

    def __str__(self):
        return self.text