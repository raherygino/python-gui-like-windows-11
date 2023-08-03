import json
import codecs
from PyQt5.QtCore import QLocale

class Translate():

    def __init__(self, lang):
        self.translations = {}
        with codecs.open('app/config/lang.json', 'r', 'utf-8') as file:
            self.translations = json.load(file)

        language = lang
        if not lang:
            language = QLocale.system().name()
            if language not in self.translations:
                language = 'fr_FR'  # Default language
        self.text = self.translations[language]