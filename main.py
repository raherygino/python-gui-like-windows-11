import sys
from view import *

def setApplication() -> QApplication:
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    return QApplication(sys.argv)

if __name__ == '__main__':
    app = setApplication()
    setTheme(Theme.DARK)
    setThemeColor("#142170", False)
    w = MainWindow()
    w.show()
    app.exec_()
