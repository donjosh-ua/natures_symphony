import threading
from PyQt5 import QtWidgets
from model.Audio import Audio
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog
from view.Ui_Registro import Ui_Registro
from controller.AnimalController import AnimalController
from controller.Procesamiento import Procesamiento


class RegistroController(QtWidgets.QMainWindow, Ui_Registro):
    
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
        self.btnAceptarCaptura.clicked.connect(self.playbuttonAccept)

    def selectAudioFile(self):

        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de audio", "", "Audio Files (*.mp3 *.flac *.ogg *.wav *.aac *.wma)") 
        
        if file_path == "" or file_path is None:
            return
           
        Audio.convert_audio_to_wav(file_path)
        self.showComponents()
        
    def hideComponents(self):
        self.btnPlay.hide()
        self.labelAcercar.hide()
        self.btnAceptarCaptura.hide()
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px;image: url(./assets/images/microfono-de-estudio.png);")

    def pressMicro(self):

        self.showComponents()
        
        # Mostrar onda de audio para indicar que se esta comenzando la grabacion del audio
        self.labelSenal.startAnimation(5)
        self.audio_thread = threading.Thread(name="hilo_secundario", target=Audio.grabar_audio, args = ())
        self.audio_thread.start()

    def showComponents(self):
        self.btnPlay.show()
        self.labelAcercar.show()
        self.btnAceptarCaptura.show()
        self.labelSenal.pressed.disconnect(self.pressMicro)
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px;image: none;")
        self.btnAlmacenamiento.hide()

    def playbuttonAccept(self):

        self.animal_controller = AnimalController()
        self.animal_controller.set_json_data(Procesamiento.find_animal(Audio.audio[1]))

        # Abrimos la ventana de AnimalController
        self.animal_controller.show()
        
    def pressPlay(self):        
        
        # Si no se ha grabado ningun audio
        if Audio.audio is None:
            print("No se ha grabado ningun audio")
            return
    
        self.labelSenal.startAnimation(5)
        self.audio_thread = threading.Thread(name="hilo_secundario", target=Audio.play_audio, args = ())
        self.audio_thread.start()