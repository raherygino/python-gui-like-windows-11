from PyQt5.QtWidgets import QFrame
from qfluentwidgets import ComboBox
from ..layout.inputLabel import InputLabel

class Select(QFrame):

    def __init__(self, label:str, items: list, parent):
        inputLabel = InputLabel(label, parent)
        self.comboBox = ComboBox(inputLabel)
        self.comboBox.addItems(items)
        self.comboBox.setCurrentIndex(0)
        self.comboBox.move(200, 200)
        inputLabel.addWidget(self.comboBox)
        parent.addWidget(inputLabel)
    
    def onChange(self, slot):
        return self.comboBox.currentTextChanged.connect(slot)