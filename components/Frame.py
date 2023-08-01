from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication,QFrame, QWidget, QHBoxLayout, QVBoxLayout

from qfluentwidgets import (CardWidget, setFont, setTheme, Theme, IconWidget, BodyLabel, CaptionLabel, PushButton,
                            TransparentToolButton, FluentIcon, RoundMenu, SubtitleLabel, Action)


class Frame(QFrame):

    def __init__(self, layoutType: str, name: str, parent=None):
        super().__init__(parent=parent)
        
        if (layoutType == "vertical"):
            self.layout = QVBoxLayout(self)
        else:
            self.layout = QHBoxLayout(self)
        
        self.setObjectName(name.replace(' ', '-'))

    def addWidget(self, widget):
        self.layout.addWidget(widget)