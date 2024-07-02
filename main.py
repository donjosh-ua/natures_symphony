from PyQt5 import QtWidgets
from PyQt6 import QtWidgets
from controller.capturarController import MainWindow
from controller.animalFoundController import AnimalFoundController
import sys

app = QtWidgets.QApplication(sys.argv)
#mainWin = MainWindow()
viewAnimalFound = AnimalFoundController()
sys.exit(app.exec())

