import threading
from PyQt5 import QtWidgets
from model.Audio import Audio
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog
from view.Ui_Registro import Ui_Registro
from controller.AnimalController import AnimalController


class RegistroController(QtWidgets.QMainWindow, Ui_Registro):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initWindow()
        self.initAction()
        
        self.show()
        self.audio_thread = None
        self.input_audio_path = None  

    def initWindow(self):
        self.setWindowTitle("Nature's Symphony")
        self.hideComponents()

    def initAction(self):
        self.btnPlay.clicked.connect(self.pressPlay)
        self.labelSenal.pressed.connect(self.pressMicro)
        self.btnAlmacenamiento.clicked.connect(self.selectAudioFile)
        self.btnAceptarCaptura.clicked.connect(self.playbuttonAccept)

    def selectAudioFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de audio", "", "Audio Files (*.mp3 *.flac *.ogg *.wav *.aac *.wma)") 
        if file_path:   
            self.input_audio_path = Audio().convert_audio_to_wav(file_path)
            self.showComponents()
        
    def hideComponents(self):
        self.btnAceptarCaptura.hide()
        self.btnPlay.hide()
        self.labelAcercar.hide()
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px;image: url(./assets/images/microfono-de-estudio.png);")

    def pressMicro(self):
        self.showComponents()
        self.input_audio_path = "./assets/output_audio.wav"
        # Mostrar onda de audio para indicar que se esta comenzando la grabacion del audio
        self.labelSenal.startAnimation(8)
        self.audio_thread = threading.Thread(name="hilo_secundario", target=Audio().grabar_audio, args = ())
        self.audio_thread.start()

    def showComponents(self):
        self.btnPlay.show()
        self.labelAcercar.show()
        self.btnAceptarCaptura.show()
        self.labelSenal.pressed.disconnect(self.pressMicro)
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px;image: none;")
        self.btnAlmacenamiento.hide()

    def playbuttonAccept(self):
        # Abrimos la ventana de AnimalController
        self.animal_controller = AnimalController()
        self.animal_controller.show()
        
    def pressPlay(self):
        # Creamos una señal que queremos que se muestre en el label por 8 segundos por ahora
        print(self.input_audio_path)
        if self.input_audio_path:
            self.labelSenal.startAnimation(8)
            self.audio_thread = threading.Thread(name="hilo_secundario", target=Audio().play_audio, args = (self.input_audio_path,))
            self.audio_thread.start()