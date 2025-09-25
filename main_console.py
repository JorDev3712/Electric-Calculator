import os

from console.controllers.appController import AppController
from util.languageManager import LanguageManager
from util.utility import Utility

folder = os.path.dirname(os.path.abspath(__file__))
languageManger = LanguageManager(folder, 'app.xml')
languageManger.set_current_language(Utility.getCurrentLanguage())
app = AppController(languageManger)
app.loader()
app.loop()