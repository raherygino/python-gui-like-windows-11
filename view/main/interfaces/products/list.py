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
        self.tableView.setItemDelegate(CustomTableItemDelegate(self.tableView))
        self.tableView.setWordWrap(False)
        self.tableView.setRowCount(60)
        self.tableView.setColumnCount(5)
        songInfos = [
            ['Gino', 'Armelin', 'Developer', '1997', '5:04'],
            ['爱你', '王心凌', '爱你', '2004', '3:39'],
            ['星のない世界', 'aiko', '星のない世界/横顔', '2007', '5:30'],
            ['横顔', 'aiko', '星のない世界/横顔', '2007', '5:06'],
            ['秘密', 'aiko', '秘密', '2008', '6:27'],
            ['シアワセ', 'aiko', '秘密', '2008', '5:25'],
            ['二人', 'aiko', '二人', '2008', '5:00'],
            ['スパークル', 'RADWIMPS', '君の名は。', '2016', '8:54'],
            ['なんでもないや', 'RADWIMPS', '君の名は。', '2016', '3:16'],
            ['前前前世', 'RADWIMPS', '人間開花', '2016', '4:35'],
            ['恋をしたのは', 'aiko', '恋をしたのは', '2016', '6:02'],
            ['夏バテ', 'aiko', '恋をしたのは', '2016', '4:41'],
            ['もっと', 'aiko', 'もっと', '2016', '4:50'],
            ['問題集', 'aiko', 'もっと', '2016', '4:18'],
            ['半袖', 'aiko', 'もっと', '2016', '5:50'],
            ['ひねくれ', '鎖那', 'Hush a by little girl', '2017', '3:54'],
            ['シュテルン', '鎖那', 'Hush a by little girl', '2017', '3:16'],
            ['愛は勝手', 'aiko', '湿った夏の始まり', '2018', '5:31'],
            ['ドライブモード', 'aiko', '湿った夏の始まり', '2018', '3:37'],
            ['うん。', 'aiko', '湿った夏の始まり', '2018', '5:48'],
            ['キラキラ', 'aikoの詩。', '2019', '5:08', 'aiko'],
            ['恋のスーパーボール', 'aiko', 'aikoの詩。', '2019', '4:31'],
            ['磁石', 'aiko', 'どうしたって伝えられないから', '2021', '4:24'],
            ['食べた愛', 'aiko', '食べた愛/あたしたち', '2021', '5:17'],
            ['列車', 'aiko', '食べた愛/あたしたち', '2021', '4:18'],
            ['花の塔', 'さユり', '花の塔', '2022', '4:35'],
            ['夏恋のライフ', 'aiko', '夏恋のライフ', '2022', '5:03'],
            ['あかときリロード', 'aiko', 'あかときリロード', '2023', '4:04'],
            ['荒れた唇は恋を失くす', 'aiko', '今の二人をお互いが見てる', '2023', '4:07'],
            ['ワンツースリー', 'aiko', '今の二人をお互いが見てる', '2023', '4:47'],
        ]
        songInfos += songInfos
        for i, songInfo in enumerate(songInfos):
            for j in range(5):
                self.tableView.setItem(i, j, QTableWidgetItem(songInfo[j]))

        self.tableView.verticalHeader().hide()
        self.tableView.setHorizontalHeaderLabels(['Title', 'Artist', 'Album', 'Year', 'Duration'])
        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView.setSortingEnabled(True)

        self.setStyleSheet("Demo{background: rgb(249, 249, 249)} ")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.addWidget(self.tableView)
        self.setObjectName(name)

'''
        self.hBoxLayout = QHBoxLayout(self)

        # NOTE: use custom item delegate
        self.setObjectName(name) '''