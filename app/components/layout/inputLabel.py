from .Frame import Frame
from qfluentwidgets import BodyLabel
from ...common.config import V_BOX

class InputLabel(Frame):

    def __init__(self, label, parent):
        super().__init__(V_BOX, name=f"col_{label.replace(' ', '-')}", parent=parent)
        self.label = BodyLabel(label)
        self.addWidget(self.label)

