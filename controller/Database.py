from pickle import dump
import os
from scipy.io.wavfile import read
import controller.Procesamiento as fngp
from os import remove


class Database:

    def __init__(self):
        self.database = {}
        self.audio_name_index = {}
        self.db_name = 'database.dat'
        self.audio_index_name = 'audio_index.dat'

    def drop_db(self):
        try:
            remove(self.db_name)
            remove(self.audio_index_name)
        except FileNotFoundError:
            pass

    def save_db(self):
        with open(self.db_name, 'wb') as db:
            dump(self.database, db, 5)

        with open(self.audio_index_name, 'wb') as audios:
            dump(self.audio_name_index, audios, 5)

    def load_db(self, folder: str):
        
        self.audio_name_index = {}
        self.database = {}
        
        for root, _, files in os.walk(folder):
            
            for file in files:
                
                if not file.endswith('.wav'):
                    continue

                full_path = os.path.join(root, file)
                animal_name = os.path.basename(root)  # This is the animal's name

                if animal_name not in self.audio_name_index:
                    self.audio_name_index[animal_name] = []
                self.audio_name_index[animal_name].append(file)
                
                print(f'Processing {animal_name}/{file}...')

                # Read the audio file
                Fs, audio_input = read(full_path)
                constellation = fngp.create_constellation(audio_input, Fs)
                hashes = fngp.create_hashes(constellation, animal_name)  # Assuming create_hashes can take animal_name as an identifier

                # Process the hashes as before
                for hash, time_index_pair in hashes.items():
                    if hash not in self.database:
                        self.database[hash] = []
                    self.database[hash].append(time_index_pair)
