import json
from PyQt5.QtCore import QLocale

class Translate():
    def __init__(self, lang):
        self.translations = {}
        with open('app/config/lang.json', 'r') as file:
            self.translations = json.load(file)

        language = lang
        if not lang:
            language = QLocale.system().name()
            if language not in self.translations:
                language = 'en_US'  # Default language
        self.text = self.translations[language]