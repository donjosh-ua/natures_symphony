import sys
from PyQt5 import QtWidgets
from controller.Entusiasta.RegistroController import RegistroController


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = RegistroController()
    # viewAnimalFound = AnimalController()
    sys.exit(app.exec())
