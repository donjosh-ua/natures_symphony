from PyQt5 import QtWidgets
from controller.RegistroController import RegistroController
from controller.AnimalController import AnimalController
import sys

app = QtWidgets.QApplication(sys.argv)
mainWin = RegistroController()
#viewAnimalFound = AnimalController()
sys.exit(app.exec())

