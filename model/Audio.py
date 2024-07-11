import sounddevice as sd
from scipy.io import wavfile
from pydub import AudioSegment
from pydub.playback import play
# from PyQt5.QtCore import QThread, pyqtSignal


class Audio():

    audio = None

    def __init__(self):
        self.audio = None

    @staticmethod
    def convert_audio_to_wav(path_audio_file):
        
        # Detectar el tipo de archivo de entrada
        formato_entrada = path_audio_file.split('.')[-1]
        
        # Leer el archivo de entrada con pydub
        audio = AudioSegment.from_file(path_audio_file, format=formato_entrada)
 
        # Exportar el archivo a WAV en el directorio especificado
        audio.export("./assets/output_audio.wav", format='wav')
        Audio.cargar_audio()
    
    @staticmethod
    def grabar_audio():
        
        time = 5
        fs = 48000
        # Grabar el audio
        audio_data = sd.rec(int(time * fs), samplerate=fs, channels=2)
        
        # El hilo secundario donde se esta grabando el audio espera que acabe con la grabacion
        sd.wait()
         
        # Guardar el archivo de audio grabado en el directorio especificado
        wavfile.write("./assets/output_audio.wav", fs, audio_data)
        Audio.cargar_audio()

    @staticmethod
    def play_audio(path=None):

        if path:
            
            fs, audio_data = wavfile.read(path)
            
            sd.play(audio_data, samplerate=fs)
            sd.wait()

            return

        # Cargar el archivo de audio
        fs, audio_data = wavfile.read("./assets/output_audio.wav")
        
        # Reproducir el audio
        sd.play(audio_data, samplerate=fs)
        sd.wait()
     
    @staticmethod
    def cargar_audio():
        Audio.audio = wavfile.read("./assets/output_audio.wav")



        
