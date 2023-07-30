from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication,QFrame, QWidget, QHBoxLayout, QVBoxLayout

from qfluentwidgets import (CardWidget, setFont, setTheme, Theme, IconWidget, BodyLabel, CaptionLabel, PushButton,
                            TransparentToolButton, FluentIcon, RoundMenu, SubtitleLabel, Action)


class AddProductFrame(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        text = "Add product"
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))