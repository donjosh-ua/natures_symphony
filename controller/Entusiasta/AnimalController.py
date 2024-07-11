from view.Ui_Animal import Ui_Animal
import sounddevice as sd
from PyQt5 import QtWidgets, QtCore, QtGui
from scipy.io import wavfile
import sys

class AnimalController(QtWidgets.QMainWindow, Ui_Animal):
    #Variable Global para saber si el usuario ya presionó el botón de play
    flagPressed = False
    jsonData={} 


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Nature's Symphony")
        self.btnPlay.clicked.connect(self.pressPlay)
        self.show()
    
    def set_json_data(self, data):
        """Establece la información del animal desde un diccionario."""
        self.jsonData = data
        self.subirInformacion()

    def subirInformacion(self):
        #Actualizamos la informacion
        self.label.setText(self.jsonData.get("nombre",""))
        pixmap = QtGui.QPixmap(self.jsonData.get("imagen", ""))
        scaled_pixmap = pixmap.scaled(151, 161, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.txtImagenAnimal.setPixmap(scaled_pixmap)
        self.txtDescripcion.setText(self.jsonData.get("descripción",""))
        self.txtHabitat.setText(self.jsonData.get("habitat",""))
        self.txtDieta.setText(self.jsonData.get("dieta",""))
        self.txtEspecies.setText(self.jsonData.get("especie",""))

         

    def pressPlay(self):
        print("Reproduciendo sonido...")
        if not self.flagPressed:
            # Reproducir sonido
            fs, audio_data = wavfile.read(self.jsonData.get("sonido",""))
            # Reproducir el audio
            sd.play(audio_data, samplerate=fs)
            self.btnPlay.setStyleSheet("background: rgb(67, 163, 32); border-radius: 10px; color:white; font: 9pt \"Papyrus\";")
            self.btnPlay.setText("Stop")
            self.flagPressed = True
        else:
            # Detener reproducción
            sd.stop()
            self.btnPlay.setStyleSheet("background: rgb(170, 255, 127); border-radius: 10px; color:black; font: 9pt \"Papyrus\";")
            self.btnPlay.setText("Play")
            self.flagPressed = False