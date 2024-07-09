import numpy as np
import sounddevice as sd
from io import BytesIO
from pydub import AudioSegment
from PyQt5.QtCore import QThread, pyqtSignal


class Audio(QThread):
    # Instancia necesaria para mandar el audio al hilo principal de la aplicacion
    audio_recorded = pyqtSignal(np.ndarray)

    def convert_audio_to_wav(self, path_audio_file):
        # Detectar el tipo de archivo de entrada
        formato_entrada = path_audio_file.split('.')[-1]
        
        # Leer el archivo de entrada con pydub
        audio = AudioSegment.from_file(path_audio_file, format=formato_entrada)
        
        # Crear un objeto BytesIO para guardar el archivo WAV en memoria
        audio_wav = BytesIO()
        
        # Exportar el archivo a WAV en el objeto BytesIO
        audio.export(audio_wav, format='wav')
        
        # Asegurarse de que el puntero esté al principio del archivo BytesIO
        audio_wav.seek(0)
        
        return audio_wav
    
    def run(self):

        #Frecuencia de muestreo usada
        fs = 44100

        #Duracion del audio
        seconds = 8
        
        #Grabar el audio
        audio_data = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        
        #El hilo secundaria donde se esta grabando el audio espera que acabe con la grabacion
        sd.wait()
        
        #Se devulve el resultado al hilo principal
        self.audio_recorded.emit(audio_data)
        
