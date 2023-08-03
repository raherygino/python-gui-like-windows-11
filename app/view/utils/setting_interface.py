# coding:utf-8
from qfluentwidgets import (SettingCardGroup, SwitchSettingCard,
                            OptionsSettingCard,
                            HyperlinkCard, PrimaryPushSettingCard, ScrollArea,
                            ExpandLayout, CustomColorSettingCard,
                            setTheme, setThemeColor)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import InfoBar
from PyQt5.QtCore import Qt, pyqtSignal, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QWidget, QLabel, QFileDialog

from ...common.icon import Icon
from ...common.config import cfg, HELP_URL, FEEDBACK_URL, AUTHOR, VERSION, YEAR, Lang
from ...common.style_sheet import StyleSheet
from ...components.layout.AppCard import AppCard
from ...common.Translate import Translate

class SettingInterface(ScrollArea):
    """ Setting interface """

    checkUpdateSig = pyqtSignal()
    musicFoldersChanged = pyqtSignal(list)
    acrylicEnableChanged = pyqtSignal(bool)
    downloadFolderChanged = pyqtSignal(str)
    minimizeToTrayChanged = pyqtSignal(bool)

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        self.currentLang = Lang().current
        self.trans = Translate(self.currentLang).text

        # setting label
        self.settingLabel = QLabel(self.trans['settings'], self)

        # personalization
        self.personalGroup = SettingCardGroup(
            self.trans['personalization'], self.scrollWidget)
        self.themeCard = OptionsSettingCard(
            cfg.themeMode,
            FIF.BRUSH,
            self.trans['app_theme_title'],
            self.trans['app_theme_details'],
            texts=[
                self.trans['light'], self.trans['dark'],
                self.trans['system_setting']
            ],
            parent=self.personalGroup
        )
        self.themeColorCard = CustomColorSettingCard(
            cfg.themeColor,
            FIF.PALETTE,
            self.trans['color_theme_title'],
            self.trans['color_theme_details'],
            self.personalGroup
        )
        self.themeColorCard.choiceLabel.setText(self.trans['color_default'])
        self.zoomCard = OptionsSettingCard(
            cfg.dpiScale,
            FIF.ZOOM,
            self.trans['interface_zoom_title'],
            self.trans['interface_zoom_details'],
            texts=[
                "100%", "125%", "150%",
                self.trans['system_setting']
            ],
            parent=self.personalGroup
        )

        '''

        self.languageCard = PrimaryPushSettingCard(
            None,
            FIF.LANGUAGE,
            'Language',
            'Set your preferred language for UI',
            self.personalGroup
        )
        
        self.comboBox = ComboBox(self)
        self.comboBox.addItems(['Français', 'English'])
        self.comboBox.setCurrentIndex(0)
        self.comboBox.currentTextChanged.connect(self.onchange)
        self.comboBox.move(200, 200)

        self.languageCard.hBoxLayout.removeWidget(self.languageCard.button)
        self.languageCard.button = None;
        self.languageCard.hBoxLayout.addWidget(self.comboBox)
        self.languageCard.hBoxLayout.setContentsMargins(14,0,14,0) '''
        # update software
        '''
        self.updateSoftwareGroup = SettingCardGroup(
            self.trans['software_update'], self.scrollWidget)
        
        self.updateOnStartUpCard = SwitchSettingCard(
            FIF.UPDATE,
            self.trans['check_for_update_title'],
            self.trans['check_for_update_details'],
            configItem=cfg.checkUpdateAtStartUp,
            parent=self.updateSoftwareGroup
        )
        self.updateOnStartUpCard.switchButton.setOnText("Activé")
        self.updateOnStartUpCard.switchButton.setOffText("Désactivé")
        '''
        # application
        self.aboutGroup = SettingCardGroup(self.trans['about'], self.scrollWidget)
        self.helpCard = HyperlinkCard(
            HELP_URL,
            self.trans['help_button'],
            FIF.HELP,
            self.trans['help_title'],
            self.trans['help_details'],
            self.aboutGroup
        )
        self.feedbackCard = PrimaryPushSettingCard(
            self.trans['feedback_title'],
            FIF.FEEDBACK,
            self.trans['feedback_title'],
            self.trans['feedback_details'],
            self.aboutGroup
        )
        
       # print()
        self.aboutCard = PrimaryPushSettingCard(
            self.trans['software_update'],
            FIF.INFO,
            self.trans['about'],
            '© ' + self.tr('Copyright') + f" {YEAR}, {AUTHOR}. " +
            self.tr('Version') + " " + VERSION,
            self.aboutGroup
        )

        self.__initWidget()

    def __initWidget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 80, 0, 20)
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.setObjectName('settingInterface')

        # initialize style sheet
        self.scrollWidget.setObjectName('scrollWidget')
        self.settingLabel.setObjectName('settingLabel')
        StyleSheet.SETTING_INTERFACE.apply(self)

        # initialize layout
        self.__initLayout()
        self.__connectSignalToSlot()

    def __initLayout(self):
        self.settingLabel.move(36, 30)

        self.personalGroup.addSettingCard(self.themeCard)
        self.personalGroup.addSettingCard(self.themeColorCard)
        self.personalGroup.addSettingCard(self.zoomCard)
        # self.personalGroup.addSettingCard(self.languageCard)
        #self.updateSoftwareGroup.addSettingCard(self.updateOnStartUpCard)

        self.aboutGroup.addSettingCard(self.helpCard)
        self.aboutGroup.addSettingCard(self.feedbackCard)
        self.aboutGroup.addSettingCard(self.aboutCard)

        # add setting card group to layout
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(36, 10, 36, 0)
        self.expandLayout.addWidget(self.personalGroup)
        #self.expandLayout.addWidget(self.updateSoftwareGroup)
        self.expandLayout.addWidget(self.aboutGroup)

    def __showRestartTooltip(self):
        """ show restart tooltip """
        InfoBar.success(
            self.tr('Updated successfully'),
            self.tr('Configuration takes effect after restart'),
            duration=1500,
            parent=self
        )
    def onchange(self, val):
        self.comboBox.setCurrentIndex(0)
        if (val == "English") :
            InfoBar.info(
                self.tr('Langue indisponible'),
                '',
                duration=2500,
                parent=self
            )
            


    def __onDownloadFolderCardClicked(self):
        """ download folder card clicked slot """
        folder = QFileDialog.getExistingDirectory(
            self, self.tr("Choose folder"), "./")
        if not folder or cfg.get(cfg.downloadFolder) == folder:
            return

        cfg.set(cfg.downloadFolder, folder)
        self.downloadFolderCard.setContent(folder)

    def __connectSignalToSlot(self):
        """ connect signal to slot """
        cfg.appRestartSig.connect(self.__showRestartTooltip)
        cfg.themeChanged.connect(setTheme)

        # personalization
        self.themeColorCard.colorChanged.connect(setThemeColor)

        # about
        self.aboutCard.clicked.connect(self.checkUpdateSig)
        self.feedbackCard.clicked.connect(
            lambda: QDesktopServices.openUrl(QUrl(FEEDBACK_URL)))
