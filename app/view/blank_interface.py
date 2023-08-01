# coding:utf-8
from qfluentwidgets import TitleLabel
from .gallery_interface import GalleryInterface
from ..common.translator import Translator

class BlankInterface(GalleryInterface):
    """ Blank interface """

    def __init__(self, parent=None):
        t = Translator()
        super().__init__(
            title=t.blank,
            subtitle='Blank page',
            parent=parent
        )
        self.setObjectName('blankInterface')
        self.title = TitleLabel('Hello world')
        self.card = self.addCard('My first card',self.title)
        self.card.setMargins(18,18,18,18)
