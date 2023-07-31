from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtGui import QPalette
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame, QApplication, QStyleOptionViewItem, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout

from qfluentwidgets import TableWidget, isDarkTheme, TitleLabel,BodyLabel, PrimaryPushButton, SearchLineEdit,StrongBodyLabel, setThemeColor, setTheme, Theme, TableView, TableItemDelegate


from qfluentwidgets import FluentIcon as FIF

class LineEdit(SearchLineEdit):
    """ Search line edit """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPlaceholderText(self.tr('Search product'))
        self.setFixedWidth(304)
        self.textChanged.connect(self.search)

class CustomTableItemDelegate(TableItemDelegate):
    """ Custom table item delegate """

    def initStyleOption(self, option: QStyleOptionViewItem, index: QModelIndex):
        super().initStyleOption(option, index)
        if index.column() != 1:
            return

        if isDarkTheme():
            option.palette.setColor(QPalette.Text, Qt.white)
            option.palette.setColor(QPalette.HighlightedText, Qt.white)
        else:
            option.palette.setColor(QPalette.Text, Qt.red)
            option.palette.setColor(QPalette.HighlightedText, Qt.red)

class ListProductsFrame(QFrame):

    def __init__(self, name: str, parent=None):
        super().__init__(parent=parent)
        #setThemeColor("#142170", False)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content_list_products = QtWidgets.QFrame(self)
        self.content_list_products.setMinimumSize(QtCore.QSize(0, 0))
        self.content_list_products.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.content_list_products.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_list_products.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_list_products.setObjectName("content_list_products")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content_list_products)
        self.horizontalLayout.setContentsMargins(12, 8, 12, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.product_col = QtWidgets.QFrame(self.content_list_products)
        self.product_col.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.product_col.setFrameShadow(QtWidgets.QFrame.Raised)
        self.product_col.setObjectName("product_col")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.product_col)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.title_list_products = TitleLabel(self.tr('Products'), self.product_col)
        self.title_list_products.setObjectName("title_list_products")
        self.verticalLayout_2.addWidget(self.title_list_products)
        self.description_list_products = BodyLabel("List products", self.product_col)
        self.description_list_products.setObjectName("description_list_products")
        self.verticalLayout_2.addWidget(self.description_list_products)
        self.frame = QtWidgets.QFrame(self.product_col)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_edit_search = LineEdit(self.frame)
        self.line_edit_search.setMaximumSize(QtCore.QSize(200, 16777215))
        self.line_edit_search.setObjectName("line_edit_search")
        self.verticalLayout_4.addWidget(self.line_edit_search)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.product_col)
        self.product_col_2 = QtWidgets.QFrame(self.content_list_products)
        self.product_col_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.product_col_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.product_col_2.setObjectName("product_col_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.product_col_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.btn_add_product = PrimaryPushButton('Add product', self.product_col_2, FIF.ADD)
        self.btn_add_product.setObjectName("btn_add_product")

        self.verticalLayout_3.addWidget(self.btn_add_product)
        self.horizontalLayout.addWidget(self.product_col_2, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.content_list_products)


        self.tableView = TableWidget(self)
        ## self.tableView.setItemDelegate(CustomTableItemDelegate(self.tableView))
        self.tableView.setWordWrap(False)
        self.tableView.setRowCount(2)
        self.tableView.setColumnCount(3)
        songInfos = [
            ['IPH3441', 'Technologies', 'Smartphone'],
            ['SMG3242', 'Technologies', 'Smartphone'],
        ]
        songInfos += songInfos
        for i, songInfo in enumerate(songInfos):
            for j in range(3):
                self.tableView.setItem(i, j, QTableWidgetItem(songInfo[j]))

        self.tableView.verticalHeader().hide()
        self.tableView.setHorizontalHeaderLabels(['Réf', 'Catégorie', 'Sous catégorie'])
        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setSortingEnabled(True)

        self.setStyleSheet("Demo{background: rgb(249, 249, 249)} ") 
        self.verticalLayout.addWidget(self.tableView)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        
        self.setObjectName(name)