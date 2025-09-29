import os

from console.controllers.appController import AppController
from util.languageManager import LanguageManager
from util.utility import Utility

# Gets the root folder
folder = os.path.dirname(os.path.abspath(__file__))
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