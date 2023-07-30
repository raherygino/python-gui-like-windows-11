from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication,QFrame, QWidget, QHBoxLayout, QVBoxLayout

from qfluentwidgets import (CardWidget, setFont, setTheme, Theme, IconWidget, BodyLabel, CaptionLabel, PushButton,
                            TransparentToolButton, FluentIcon, RoundMenu, SubtitleLabel, Action)


class ListInvoicesFrame(QFrame):

    def __init__(self, name: str, parent=None):
        super().__init__(parent=parent)
        text = "List invoices"
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(name)