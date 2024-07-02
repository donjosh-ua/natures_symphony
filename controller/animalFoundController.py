from view.ViewAnimalFound import Ui_NuevoRegistro
from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class AnimalFoundController(QtWidgets.QMainWindow, Ui_NuevoRegistro):
    #Variable Global para saber si el usuario ya presionó el botón de play
    flagPressed = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Nature's Symphony")
        self.btnPlay.clicked.connect(self.pressPlay)
        self.show()
    # Datos del animal
    animal_data = {
        "nombre": "León",
        "imagen": "./assets/images/leon.jpg",
        "descripción": "El león es un mamífero carnívoro con un tono amarrillo anaranjado.",
        "habitat": "Sabanas, praderas y matorrales abiertos de África subsahariana.",
        "dieta": "Carnívoro, se alimenta principalmente de ungulados grandes.",
        "especie": "Panthera leo",
        "sonido": "ruta/a/la/carpeta/del/sonido/leon.mp3"
    }

    def subirInformacion(self):
        print("Subiendo información...")

    def pressPlay(self):
        print("Reproduciendo sonido...")
        if not self.flagPressed:
            self.btnPlay.setStyleSheet("background: rgb(67, 163, 32); border-radius: 10px; color:white; font: 9pt \"Papyrus\";")
            self.btnPlay.setText("Stop")
            self.flagPressed = True
        else:
            self.btnPlay.setStyleSheet("background: rgb(170, 255, 127); border-radius: 10px; color:black; font: 9pt \"Papyrus\";")
            self.btnPlay.setText("Play")
            self.flagPressed = False
        

        

    
    