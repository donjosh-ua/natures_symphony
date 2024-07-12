import threading
from PyQt5 import QtWidgets, QtCore
from model.Procesamiento.Audio import Audio
from PyQt5.QtWidgets import QFileDialog
from view.Ui_Registro import Ui_Registro
from controller.Entusiasta.AnimalController import AnimalController
from model.Procesamiento.Procesamiento import Procesamiento
from pydub import AudioSegment


class RegistroController(QtWidgets.QMainWindow, Ui_Registro):
    
    registered_animals = []

    def __init__(self):

        super().__init__()

        self.setupUi(self)
        self.initWindow()
        self.initAction()
        self.show()
        self.audio_thread = None
        self.permisos_microfono = False
        self.permisos_almacenamiento = False
        
    def initWindow(self):
        self.setWindowTitle("Nature's Symphony")
        self.hideComponents()

    def initAction(self):
        self.btnPlay.clicked.connect(self.pressPlay)
        self.labelSenal.pressed.connect(self.pressMicro)
        self.btnAlmacenamiento.clicked.connect(self.selectAudioFile)
        self.btnAceptarCaptura.clicked.connect(self.playbuttonAccept)
        self.btnRegresarPrincipal.clicked.connect(self.pushReturn)

    def selectAudioFile(self):

        # Verificar si los permisos ya fueron otorgados
        if not self.permisos_almacenamiento:
            # Mostrar ventana emergente para solicitar permisos
            reply = QtWidgets.QMessageBox.question(self, 'Permiso de Almacenamiento', 
                                    '¿Permitir acceso al almacenamiento?', 
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            
            if reply == QtWidgets.QMessageBox.Yes:
                self.permisos_almacenamiento = True
            else:
                self.permisos_almacenamiento = False
                return  # Salir de la función si no se otorgaron los permisos

        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo de audio", "", "Audio Files (*.mp3 *.flac *.ogg *.wav *.aac *.wma)") 
        
        if file_path == "" or file_path is None:
            return
        
        # Verificar si el archivo de audio es corrupto
        try:
            # Intenta cargar el archivo usando pydub
            AudioSegment.from_file(file_path)
            
            # Alternativamente, puedes usar soundfile para verificar
            # data, samplerate = sf.read(file_path)
         
        except Exception as e:
            # Si ocurre un error, mostrar un pop up indicando que el archivo está corrupto
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Problemas con el audio ingresado")
            msg.setWindowTitle("Error")
            msg.exec_()

            return
        
        Audio.convert_audio_to_wav(file_path)
        self.showComponents2()

        
    def hideComponents(self):
        self.btnPlay.hide()
        self.labelAcercar.hide()
        self.btnAceptarCaptura.hide()
        self.btnRegresarPrincipal.hide()
        self.btnAlmacenamiento.show()
        self.labelSenal.pressed.connect(self.pressMicro)
        self.showMicrophoneImage()
    
    def pressMicro(self):
        # Verificar si los permisos ya fueron otorgados
        if not self.permisos_microfono:
            # Mostrar ventana emergente para solicitar permisos
            reply = QtWidgets.QMessageBox.question(self, 'Permiso de Micrófono', 
                                    '¿Permitir acceso al micrófono?', 
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            
            if reply == QtWidgets.QMessageBox.Yes:
                self.permisos_microfono = True
            else:
                self.permisos_microfono = False
                return  # Salir de la función si no se otorgaron los permisos
        
        # Si los permisos ya fueron otorgados o se acaban de otorgar
        self.showComponents()

        # Mostrar onda de audio para indicar que se está comenzando la grabación del audio
        self.labelSenal.startAnimation(5)
        self.audio_thread = threading.Thread(name="hilo_secundario", target=Audio.grabar_audio, args=())
        self.audio_thread.start()
        QtCore.QTimer.singleShot(5000, self.showMicrophoneImage)

    def showMicrophoneImage(self):
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px; image: url(./assets/images/microfono-de-estudio.png);")

    def showComponents(self):
        self.btnPlay.show()
        self.labelAcercar.show()
        self.btnAceptarCaptura.show()
        self.labelSenal.pressed.disconnect(self.pressMicro)
        self.btnRegresarPrincipal.show()
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px;image: none;")
        self.btnAlmacenamiento.hide()

    def showComponents2(self):
        self.btnPlay.show()
        self.btnAceptarCaptura.show()
        self.btnRegresarPrincipal.show()
        self.labelSenal.pressed.disconnect(self.pressMicro)
        self.showMicrophoneImage()
        self.btnAlmacenamiento.hide()


    def playbuttonAccept(self):

        animal_info = Procesamiento.find_animal(Audio.audio[1])
        animal_name = animal_info.get("nombre", None)

        print(self.registered_animals)
        print(f"Animal encontrado: {animal_name}")

        if animal_info is None:
            msg = QtWidgets.QMessageBox()
            # msg.setIcon(QtWidgets.QMessageBox.information)
            msg.setText("No se han encontrado coincidencias")
            msg.setWindowTitle("Información")
            msg.exec_()
            return

        if animal_name in self.registered_animals:
            msg = QtWidgets.QMessageBox()
            # msg.setIcon(QtWidgets.QMessageBox.information)
            msg.setText(f"Animal \'{animal_name}\' ya registrado")
            msg.setWindowTitle("Información")
            msg.exec_()
            return
        
        self.registered_animals.append(animal_name)

        self.animal_controller = AnimalController()
        self.animal_controller.set_json_data(animal_info)

        # Abrimos la ventana de AnimalController
        self.animal_controller.show()
    
    def pushReturn(self):
        self.hideComponents()
        
    def pressPlay(self):        
        self.labelSenal.setStyleSheet("background: rgb(170, 255, 127); border-radius: 100px;image: None;")
        # Si no se ha grabado ningun audio
        if Audio.audio is None:
            print("No se ha grabado ningun audio")
            return
    
        self.labelSenal.startAnimation(5)
        self.audio_thread = threading.Thread(name="hilo_secundario", target=Audio.play_audio, args = ())
        self.audio_thread.start()
        QtCore.QTimer.singleShot(5000, self.showMicrophoneImage)