from view.defaultView import Ui_NuevoRegistro
from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class MainWindow(QtWidgets.QMainWindow, Ui_NuevoRegistro):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Nature's Symphony")
        self.hideComponents()
        self.labelSenal.pressed.connect(self.pressMicro)
        self.labelSenal.released.connect(self.releasedMicro)
        self.btnPlay.clicked.connect(self.pressPlay)
        self.show()
    
    def hideComponents(self):
        self.btnAceptarCaptura.hide()
        self.btnPlay.hide()
        self.labelAcercar.hide()
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px;image: url(./assets/images/microfono-de-estudio.png);")

    def pressMicro(self):
        print("Presionando Micro...")
    
    def releasedMicro(self):
        print("Cambiando interfaz...")
        self.labelAcercar.show()
        self.btnPlay.show()
        self.btnAceptarCaptura.show()
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px;image: none;")
        self.btnAlmacenamiento.hide()
    
    def pressPlay(self):
        print("Reproduciendo...")
        # Creamos una señal que queremos que se muestre en el label por 10 segundos por ahora
        self.labelSenal.startAnimation(5)