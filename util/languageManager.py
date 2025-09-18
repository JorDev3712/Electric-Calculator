import os
import xml.etree.ElementTree as xmlTree
from dominion.language import Language

class LanguageManager:
    def __init__(self, root_folder: str, fileName: str):
        self.languages = dict()
        self._filePath = os.path.join(root_folder, fileName)
        self._tree = None

    def __add_new_language(self, id: str, code: str, text: str):
        key = f'{id}_{code}'
        lan = Language(code, text)
        if key in self.languages:
            print(f'This key={key} has been added previously')
        else:
            self.languages[key] = lan

    # Sets the id language to quickly get a code word
    def set_current_language(self, id: str):
        self.id_language = id

    def get_word(self, code: str)->Language | None:
        if self.id_language is None:
            print('It is necessary to set the current id language')
            return None

        key = f'{self.id_language}_{code}'
        if key in self.languages:
            return self.languages[key]
        else:
            None

    def load(self):
        self._tree = xmlTree.parse(self._filePath)
        root = self._tree.getroot()
        print('Loading xml....')
        # Finding the language elements
        for lanElement in root.findall('language'):
            # Gets the value of the def attribute
            id = lanElement.get('def')
            print(f'Language code={id} found! Searching for words...')
            # Finding the word elements
            counter_words = 0
            for wordElement in lanElement.findall('word'):
                self.__add_new_language(id, wordElement.get('code'), wordElement.get('text'))
                counter_words += 1
            print(f'{counter_words} words found')
            