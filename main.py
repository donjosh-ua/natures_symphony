from PyQt5 import QtWidgets
from controller.RegistroController import RegistroController
from controller.AnimalController import AnimalController
import sys
from controller.Procesamiento import Procesamiento
from scipy.io.wavfile import read



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = RegistroController()
    # viewAnimalFound = AnimalController()
    sys.exit(app.exec())

    # Fs, audio_input = read('dog_example.wav')
    # print(Procesamiento.find_animal(audio_input, Fs))