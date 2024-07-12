import sys
from PyQt5 import QtWidgets
from controller.Entusiasta.RegistroController import RegistroController
from model.Procesamiento.Database import Database


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mainWin = RegistroController()
    sys.exit(app.exec())
