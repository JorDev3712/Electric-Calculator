import ctypes

class Utility:

    @staticmethod
    def parseInt(textValue: str)->tuple:
        try:
            number = int(textValue)
            return (True, number)
        except:
            return (False, 0)
        
    @staticmethod
    def parseFloat(textValue: str)->tuple:
        try:
            number = float(textValue)
            return (True, number)
        except:
            return (False, 0)

    @staticmethod
    def __getKeyBoardLayoutName():
        try:
            user32 = ctypes.windll.user32
            layout_id = user32.GetKeyboardLayout(0) & 0xFFFF
            return layout_id
        except Exception as e:
            return f"Error: {e}"
        
    @classmethod
    def getCurrentLanguage(cls)->str:
        id = cls.__getKeyBoardLayoutName()
        if id == 3082 or id == 2058 or 10250:
            return 'es'
        else:
            return 'en'