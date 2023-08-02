from PyQt5.QtWidgets import QFrame
from qfluentwidgets import LineEdit
from ..layout.inputLabel import InputLabel

class InputText(QFrame):

    def __init__(self, label: str, parent):
        inputLabel = InputLabel(label, parent)
        self.lineEdit = LineEdit(inputLabel)
        inputLabel.addWidget(self.lineEdit)
        parent.addWidget(inputLabel)
    
    def text(self)-> str :
        return self.lineEdit.text()

    def setText(self, text:str):
        self.lineEdit.setText(text)