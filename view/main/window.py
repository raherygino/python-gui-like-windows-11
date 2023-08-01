# coding:utf-8
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QLabel, QApplication, QFrame, QHBoxLayout, QVBoxLayout
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition, SearchLineEdit, setThemeColor)
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, TitleBar

from .interfaces import *

class CustomTitleBar(TitleBar):
    """ Title bar with icon and title """

    def __init__(self, parent):
        super().__init__(parent)
        self.setFixedHeight(48)
        self.hBoxLayout.removeWidget(self.minBtn)
        self.hBoxLayout.removeWidget(self.maxBtn)
        self.hBoxLayout.removeWidget(self.closeBtn)

        # add window icon
        self.iconLabel = QLabel(self)
        self.iconLabel.setFixedSize(18, 18)
        self.hBoxLayout.insertSpacing(0, 20)
        self.hBoxLayout.insertWidget(
            1, self.iconLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        self.window().windowIconChanged.connect(self.setIcon)

        # add title label
        self.titleLabel = QLabel(self)
        self.hBoxLayout.insertWidget(
            2, self.titleLabel, 0, Qt.AlignLeft | Qt.AlignVCenter)
        self.titleLabel.setObjectName('titleLabel')
        self.window().windowTitleChanged.connect(self.setTitle)

        # add search line edit
        self.searchLineEdit = SearchLineEdit(self)
        self.searchLineEdit.setPlaceholderText('搜索应用、游戏、电影、设备等')
        self.searchLineEdit.setFixedWidth(400)
        self.searchLineEdit.setClearButtonEnabled(True)

        self.vBoxLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setSpacing(0)
        self.buttonLayout.setContentsMargins(0, 0, 0, 0)
        self.buttonLayout.setAlignment(Qt.AlignTop)
        self.buttonLayout.addWidget(self.minBtn)
        self.buttonLayout.addWidget(self.maxBtn)
        self.buttonLayout.addWidget(self.closeBtn)
        self.vBoxLayout.addLayout(self.buttonLayout)
        self.vBoxLayout.addStretch(1)
        self.hBoxLayout.addLayout(self.vBoxLayout, 0)

    def setTitle(self, title):
        self.titleLabel.setText(title)
        self.titleLabel.adjustSize()

    def setIcon(self, icon):
        self.iconLabel.setPixmap(QIcon(icon).pixmap(18, 18))

    def resizeEvent(self, e):
        self.searchLineEdit.move((self.width() - self.searchLineEdit.width()) //2, 8)

class MainWidget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))

class MainWindow(FluentWindow):

    def __init__(self):
        super().__init__()
    

        # create sub interface
        self.homeInterface = HomeFrame()

        self.listProductsInterface = ListProductsFrame("list_prod_1")
        self.listProductsInterface2 = ListProductsFrame("list_prod_2")
        self.addProductInterface = AddProductFrame()

        self.listInvoicesInterface = ListInvoicesFrame("list_inv_1")
        self.listInvoicesInterface2 = ListInvoicesFrame("list_inv_2")
        self.addInvoiceInterface = AddInvoiceFrame()
        self.settingInterface = SettingsFrame()
        self.initNavigation()
        self.initWindow()



    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, 'Home')
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.listProductsInterface, FIF.APPLICATION, 'Products', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.addProductInterface, FIF.FOLDER_ADD, 'New product', parent=self.listProductsInterface)
        self.addSubInterface(self.listProductsInterface2, FIF.FOLDER, 'List products', parent=self.listProductsInterface)
        self.addSubInterface(self.listInvoicesInterface, FIF.DOCUMENT, 'Invoices', NavigationItemPosition.SCROLL)
        self.addSubInterface(self.addInvoiceInterface, FIF.FOLDER_ADD, 'New Invoices', parent=self.listInvoicesInterface)
        self.addSubInterface(self.listInvoicesInterface2, FIF.FOLDER, 'List Invoices', parent=self.listInvoicesInterface)

        # add custom widget to bottom
        
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('Georginot Armelin', 'resources/user.png'),
            #onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

        ''' add badge to navigation item
        item = self.navigationInterface.widget(self.videoInterface.objectName())
        InfoBadge.attension(
            text=9,
            parent=item.parent(),
            target=item,
            position=InfoBadgePosition.NAVIGATION_ITEM
        ) '''

    def initWindow(self):
        self.resize(900, 700)
        # self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        # self.setWindowTitle('Invoice App')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def closeEvent(self, event):
        w = MessageBox(
            'Fermer l\'application',
            'Toutes les données qui ne sont pas sauvegardés seront perdus.\nVoulez-vous fermer l\'application vraiment?',
            self
        )
        w.yesButton.setText('Oui')
        w.cancelButton.setText('Non')

        if w.exec():
            sys.exit()
        else:
            event.ignore()
            