from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt
from qfluentwidgets import CheckBox
from ..layout.inputLabel import InputLabel

class InputCheck(QFrame):

    def __init__(self, label: str, text:str, parent):
        inputLabel = InputLabel(label, parent)
        self.checkBox = CheckBox(text, inputLabel)
        #self.checkBox.setTristate(True)
        inputLabel.addWidget(self.checkBox)
        parent.layout.addWidget(inputLabel,0, Qt.AlignTop)

    def setText(self, text:str):
        self.checkBox.setText(text)