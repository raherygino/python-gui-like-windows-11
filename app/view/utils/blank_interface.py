# coding:utf-8
from .gallery_interface import GalleryInterface
from ...common.translator import Translator
from ...common.Translate import Translate
from ...common.config import Lang
from ...components import *
from qfluentwidgets import BodyLabel

class BlankInterface(GalleryInterface):
    """ Blank interface """

    def __init__(self, parent=None):
        t = Translator()
        self.trans = Translate(Lang().current).text
        super().__init__(
            title=t.blank,
            subtitle='Blank page',
            parent=parent
        )

        self.row = Frame('horizontal', 'row_1', parent=parent)
        self.label = BodyLabel(self.trans['hello'])
        self.row.addWidget(self.label)

        self.addCard('Blank card', self.row)

        #self.card.setMargins(18,18,18,18)

        self.setObjectName('blankInterface')
