import os
import sys

from console.controllers.appController import AppController
from util.languageManager import LanguageManager
from util.utility import Utility

def get_app_folder():
    if getattr(sys, 'frozen', False):
        # Ejecutable empaquetado
        return os.path.dirname(sys.executable)
    else:
        # Script de Python normal
        return os.path.dirname(os.path.abspath(__file__))

# Gets the root folder
folder = get_app_folder()
languageManger = LanguageManager(folder, 'app.xml')

# Sets common language
languageManger.set_current_language(Utility.getCurrentLanguage())

print('***************************************')
print(f'*** {languageManger.get_word('app_by')} JorDev3712 ***')
print('***************************************')
print('')

# Create app
app = AppController(languageManger)
app.loader()
app.loop()