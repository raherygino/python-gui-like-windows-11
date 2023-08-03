from .Frame import Frame
from qfluentwidgets import BodyLabel
from ...common.config import V_BOX
from PyQt5.QtCore import Qt

class InputLabel(Frame):

    def __init__(self, label, parent):
        super().__init__(V_BOX, name=f"col_{label.replace(' ', '-')}", parent=parent)
        self.label = BodyLabel(label)
        self.layout.addWidget(self.label,0, Qt.AlignTop)

