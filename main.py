from PyQt5 import QtWidgets
from view.defaultView import Ui_NuevoRegistro
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_NuevoRegistro):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())