# coding:utf-8
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,
                            InfoBadgePosition)
from qfluentwidgets import FluentIcon as FIF

from .interfaces import *


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
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('Invoice App')

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
            