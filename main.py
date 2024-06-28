from PyQt5 import QtWidgets
from controller.capturarController import MainWindow
import sys

app = QtWidgets.QApplication(sys.argv)
mainWin = MainWindow()
sys.exit(app.exec_())