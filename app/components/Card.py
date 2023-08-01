from PyQt5.QtCore import Qt
from .ExampleCard import ExampleCard

class Card():
    
    def __init__(self, title, widget, view, parent):
        self.card = ExampleCard(title, widget, "", 0, view)
        parent.addWidget(self.card, 0, Qt.AlignTop)
    
    def setMargins(self: int, left: int, top: int, right: int, bottom: int):
        self.card.bottomLayout.setContentsMargins(left, top, right, bottom)