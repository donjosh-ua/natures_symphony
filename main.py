# from PyQt5 import QtWidgets
# from controller.RegistroController import RegistroController
# from controller.AnimalController import AnimalController
from scipy.io.wavfile import read
from controller.database import Database
import controller.buscador as buscador 
# import sys


if __name__ == '__main__':
    # app = QtWidgets.QApplication(sys.argv)
    mainWin = RegistroController()
    # viewAnimalFound = AnimalController()
    # sys.exit(app.exec())
