# coding: utf-8
from PyQt5.QtCore import QUrl, QSize
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication

from qfluentwidgets import NavigationAvatarWidget, NavigationItemPosition, MessageBox, FluentWindow, SplashScreen
from qfluentwidgets import FluentIcon as FIF

from .utils.gallery_interface import GalleryInterface
from .utils.setting_interface import SettingInterface
from .utils.blank_interface import BlankInterface
from .utils.widgets_interface import WidgetsInterface
from .utils.table_view_interface import TableViewInterface

from .home.home_interface import HomeInterface

from ..common.config import SUPPORT_URL, Lang
from ..common.signal_bus import signalBus
from ..common.translator import Translator
from ..common.Translate import Translate
from ..common import resource

class MainWindow(FluentWindow):

    def __init__(self):
        super().__init__()
        self.initWindow()
        self.trans = Translate(Lang().current).text

        # create sub interface
        self.homeInterface = HomeInterface(self)
        self.widgetsInterface = WidgetsInterface(self)
        self.tableViewInterface = TableViewInterface(self)
        self.blankInterface = BlankInterface(self)
        self.settingInterface = SettingInterface(self)
        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()
        self.splashScreen.finish()

    def initLayout(self):
        signalBus.switchToSampleCard.connect(self.switchToSample)
        signalBus.supportSignal.connect(self.onSupport)

    def initNavigation(self):
        # add navigation items
        t = Translator()
        self.addSubInterface(self.homeInterface, FIF.HOME, "Home")
        self.addSubInterface(self.widgetsInterface, FIF.GAME, self.trans['widgets'])
        self.addSubInterface(self.tableViewInterface, FIF.LAYOUT, self.trans['table_view'])
        self.addSubInterface(self.blankInterface, FIF.DOCUMENT, t.blank)
        self.navigationInterface.addSeparator()
        pos = NavigationItemPosition.SCROLL
        
        # add custom widget to bottom
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('Georginot', 'app/resource/images/user.png'),
            onClick=self.onSupport,
            position=NavigationItemPosition.BOTTOM
        )
        
        self.addSubInterface(
            self.settingInterface, FIF.SETTING, self.tr('Settings'), NavigationItemPosition.BOTTOM)
        

    def initWindow(self):
        self.resize(960, 670)
        self.setMinimumWidth(760)
        self.setWindowIcon(QIcon('app/resource/images/logo.png'))
        self.setWindowTitle('PyQt-Fluent-Widgets')
        
        # create splash screen
        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()
        

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        self.show()
        QApplication.processEvents()

    def onSupport(self):
        w = MessageBox(
            'Voir mon profile',
            'Vous voulez voir mon profil dans le web ?',
            self
        )
        w.yesButton.setText('Oui')
        w.cancelButton.setText('Non')
        if w.exec():
            QDesktopServices.openUrl(QUrl(SUPPORT_URL))

    def switchToSample(self, routeKey, index):
        """ switch to sample """
        interfaces = self.findChildren(GalleryInterface)
        for w in interfaces:
            if w.objectName() == routeKey:
                self.stackedWidget.setCurrentWidget(w, False)
                w.scrollToCard(index)
