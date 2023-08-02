# coding:utf-8
from .gallery_interface import GalleryInterface
from ...common.translator import Translator
from ...common.Translate import Translate
from ...common.config import Lang
from ...components import *

class BlankInterface(GalleryInterface):
    """ Blank interface """

    def __init__(self, parent=None):
        t = Translator()
        trans = Translate(Lang().current)
        super().__init__(
            title=t.blank,
            subtitle='Blank page',
            parent=parent
        )

        self.row = Frame('horizontal', 'row_1', parent=parent)
        self.inputFirstName = InputText(trans.text['hello'], self.row)
        self.inputLastName = InputText("Lastname", self.row)
        self.selectGenre = Select("Genre", ["Female", "Male"], self.row)
        self.addCard('Blank card', self.row)

        #self.card.setMargins(18,18,18,18)

        self.setObjectName('blankInterface')
