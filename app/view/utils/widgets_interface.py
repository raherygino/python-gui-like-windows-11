# coding:utf-8
from .gallery_interface import GalleryInterface
from ...common.Translate import Translate
from ...common.config import Lang
from ...components import *
from qfluentwidgets import RadioButton, BodyLabel, SpinBox,SwitchButton, TimeEdit, DateEdit,DateTimeEdit, DoubleSpinBox, CalendarPicker
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout

class WidgetsInterface(GalleryInterface):
    """ Widgets interface """

    def __init__(self, parent=None):
        self.trans = Translate(Lang().current).text
        super().__init__(
            title=self.trans['widgets'],
            subtitle='Widgets page',
            parent=parent
        )

        self.content = Frame('vertical', 'content', parent=parent)
        self.row = Frame('vertical', 'row', parent=parent)
        self.inputFirstName = InputText(self.trans['line_edit'], self.row)
        self.selectGenre = Select(self.trans['combox'], ["Options 1", "Options 2"], self.row)
        self.checkbox = InputCheck(self.trans['checkbox'], self.trans['yes'], self.row)
    
        self.col = Frame('vertical', 'row', parent=parent)

        self.labelRadio = BodyLabel(self.trans['radio_button'])

        self.button1 = RadioButton('Option 1', self)
        self.button2 = RadioButton('Option 2', self)
        self.button3 = RadioButton('Option 3', self)

        self.labelSpinBox = BodyLabel(self.trans['spin_box'])
        self.spinBox = SpinBox(self)
        self.timeEdit = TimeEdit(self)
        self.dateEdit = DateEdit(self)
        self.dateTimeEdit = DateTimeEdit(self)
        self.doubleSpinBox = DoubleSpinBox(self)

        
        self.labelDatePicker = BodyLabel(self.trans['date_picker'])
        self.picker = CalendarPicker(self)
        self.picker.dateChanged.connect(print)

        
        self.labelSwitchButton = BodyLabel(self.trans['switch_button'])
        self.switchButton = SwitchButton(self)
        self.switchButton.checkedChanged.connect(print)

        self.col.addWidget(self.labelRadio)
        self.col.addWidget(self.button1)
        self.col.addWidget(self.button2)
        self.col.addWidget(self.button3)

        self.col.addWidget(self.labelSpinBox)
        self.col.addWidget(self.spinBox)
        self.col.addWidget(self.timeEdit)
        self.col.addWidget(self.dateEdit)
        self.col.addWidget(self.dateTimeEdit)
        self.col.addWidget(self.doubleSpinBox)

        self.col.addWidget(self.labelDatePicker)
        self.col.addWidget(self.picker)

        self.col.addWidget(self.labelSwitchButton)
        self.col.addWidget(self.switchButton)

        self.row.addWidget(self.col)
        self.content.addWidget(self.row)
        self.addCard(self.trans['card'], self.content)

        self.setObjectName('widgetsInterface')
