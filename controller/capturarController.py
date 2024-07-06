from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSlot
import numpy as np
from view.defaultView import Ui_NuevoRegistro
from model.Audio import Audio

class MainWindow(QtWidgets.QMainWindow, Ui_NuevoRegistro):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initWindow()
        self.initAction()
        self.show()
        self.audio_thread = None

    def initWindow(self):
        self.setWindowTitle("Nature's Symphony")
        self.hideComponents()

    def initAction(self):
        self.btnPlay.clicked.connect(self.pressPlay)
        self.labelSenal.pressed.connect(self.pressMicro)
        self.btnAlmacenamiento.clicked.connect(self.selectAudioFile)

    def selectAudioFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de audio", "", "Audio Files (*.mp3 *.flac *.ogg *.wav *.aac *.wma)") 
        if file_path:   
            self.input_audio = Audio().convert_audio_to_wav(file_path)
            self.showComponents()
        
    def hideComponents(self):
        self.btnAceptarCaptura.hide()
        self.btnPlay.hide()
        self.labelAcercar.hide()
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px;image: url(./assets/images/microfono-de-estudio.png);")

    def pressMicro(self):
        self.showComponents()
        #Mostrar onda de audio para indicar que se esta comenzando la grabacion del audio
        self.pressPlay()
        #Inicializar hilo secundario para realizar grabacion
        self.audio_thread = Audio()
        #Se indica accion a relizar en el hilo secundario
        self.audio_thread.audio_recorded.connect(self.on_audio_recorded)
        self.audio_thread.start()

    def showComponents(self):
        self.labelAcercar.show()
        self.btnAceptarCaptura.show()
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px;image: none;")
        self.btnAlmacenamiento.hide()

    @pyqtSlot(np.ndarray)
    def on_audio_recorded(self, audio_data):
        self.input_audio = audio_data
        
    def pressPlay(self):
        # Creamos una señal que queremos que se muestre en el label por 8 segundos por ahora
        self.labelSenal.startAnimation(6)