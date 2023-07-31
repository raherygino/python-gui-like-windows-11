
from PyQt5.QtWidgets import QFrame, QApplication, QStyleOptionViewItem, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout


class TableView(TableWidget):

    def __init__(self, parent):
        self.tableView = TableWidget(self)
        self.tableView.setItemDelegate(CustomTableItemDelegate(self.tableView))
        self.tableView.setWordWrap(False)
        self.tableView.setRowCount(2)
        self.tableView.setColumnCount(5)
        songInfos = [
            ['IPH3441', 'iPhone 14 Pro Max', 'Technologies', 'Smartphone', '5 000 000 MGA'],
            ['SMG3242', 'Samsung S23 Ultra', 'Technologies', 'Smartphone', '4 000 000 MGA'],
        ]
        songInfos += songInfos
        for i, songInfo in enumerate(songInfos):
            for j in range(5):
                self.tableView.setItem(i, j, QTableWidgetItem(songInfo[j]))

        self.tableView.verticalHeader().hide()
        self.tableView.setHorizontalHeaderLabels(['Réf', 'Désignation', 'Catégorie', 'Sous catégorie', 'Prix'])
        #self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setSortingEnabled(True)

        self.setStyleSheet("Demo{background: rgb(249, 249, 249)} ")
        parent.addWidget(self.tableView)




