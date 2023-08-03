# coding:utf-8
from .gallery_interface import GalleryInterface
from ...common.translator import Translator
from ...common.Translate import Translate
from ...common.config import Lang
from ...components import *

from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from qfluentwidgets import TableWidget

class TableViewInterface(GalleryInterface):
    """ TableView interface """

    def __init__(self, parent=None):
        t = Translator()
        self.trans = Translate(Lang().current).text
        super().__init__(
            title=self.trans['table_view'],
            subtitle='TableView page',
            parent=parent
        )

        self.contentTableInterface = Frame('vertical', 'contentTableInterface', parent=parent)

        self.tableView = TableWidget(self)
        self.tableView.setWordWrap(False)
        self.tableView.setRowCount(5)
        self.tableView.setColumnCount(5)
        songInfos = [
            ['data 1.1', 'data 1.2', 'data 1.3', 'data 1.4', 'data 1.5'],
            ['data 2.1', 'data 2.2', 'data 2.3', 'data 2.4', 'data 2.5'],
            ['data 3.1', 'data 3.2', 'data 3.3', 'data 3.4', 'data 3.5'],
            ['data 4.1', 'data 4.2', 'data 4.3', 'data 4.4', 'data 4.5'],
            ['data 5.1', 'data 5.2', 'data 5.3', 'data 5.4', 'data 5.5'],
        ]
        songInfos += songInfos
        for i, songInfo in enumerate(songInfos):
            for j in range(5):
                self.tableView.setItem(i, j, QTableWidgetItem(songInfo[j]))

        self.tableView.verticalHeader().hide()
        self.tableView.setHorizontalHeaderLabels(['Header 01', 'Header 02', 'Header 03', 'Header 04', 'Header 05'])
        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.contentTableInterface.addWidget(self.tableView)
        
        self.addCard('TableView card', self.contentTableInterface)
        self.setObjectName('tableInterface')
