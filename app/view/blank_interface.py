# coding:utf-8
from .gallery_interface import GalleryInterface
from ..common.translator import Translator
from ..components import *

class BlankInterface(GalleryInterface):
    """ Blank interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title=t.blank,
            subtitle='Blank page',
            parent=parent
        )

        self.row = Frame('horizontal', 'row_1', parent=parent)
        self.inputFirstName = InputText("Firstname", self.row)
        self.inputLastName = InputText("Lastname", self.row)
        self.selectGenre = Select("Genre", ["Female", "Male"], self.row)
        self.addCard('Blank card', self.row)

        #self.card.setMargins(18,18,18,18)

        self.setObjectName('blankInterface')
