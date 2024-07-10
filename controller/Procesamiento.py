from pickle import load
from scipy import signal
from scipy.io.wavfile import read
import json
import numpy as np


class Procesamiento:

    def score_hashes_against_database(hashes, database):

        matches_per_audio = {}
        for hash, (sample_time, _) in hashes.items():
            if hash in database:
                matching_occurences = database[hash]
                for source_time, audio_index in matching_occurences:
                    if audio_index not in matches_per_audio:
                        matches_per_audio[audio_index] = []
                    matches_per_audio[audio_index].append((hash, sample_time, source_time))
                
        scores = {}
        for audio_index, matches in matches_per_audio.items():
            audio_scores_by_offset = {}
            for hash, sample_time, source_time in matches:
                delta = source_time - sample_time
                if delta not in audio_scores_by_offset:
                    audio_scores_by_offset[delta] = 0
                audio_scores_by_offset[delta] += 1

            max = (0, 0)
            for offset, score in audio_scores_by_offset.items():
                if score > max[1]:
                    max = (offset, score)
            
            scores[audio_index] = max

        # Sort the scores for the user
        scores = list(sorted(scores.items(), key=lambda x: x[1][1], reverse=True)) 
        
        return scores

    @staticmethod
    def find_animal(audio_input, Fs):

        try:
            database = load(open('database.dat', 'rb'))
            audio_name_index = load(open('audio_index.dat', 'rb'))
        except FileNotFoundError:
            print("Database or audio index file not found.")
            return []
        
        constellation = Procesamiento.create_constellation(audio_input, Fs)
        hashes = Procesamiento.create_hashes(constellation, None)
        scores = Procesamiento.score_hashes_against_database(hashes, database)
        total_score = sum(score[1][1] for score in scores)

        if total_score == 0:
            return [("No matches found", 1.0)]

        return Procesamiento.get_animal_info(scores[0][0])

    @classmethod
    def get_animal_info(cls, animal_name):

        # Load the JSON data
        with open('./animals.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Search for the animal
        for animal in data['animals']:
            if animal['nombre'].lower() == animal_name.lower():
                return animal
        
        # If no animal is found
        return None

    @classmethod
    def create_constellation(audio, Fs, window_length=0.5, num_peaks=12):
    
        # Determina si el audio esta en uno o dos canales
        if audio.ndim == 1 :
            audio = audio.reshape(-1)
        else :
            audio = audio[:, 0].ravel()
            
        window_length_samples = (lambda x: x + x % 2)(int(window_length * Fs))
        constellation_map = []
        amount_to_pad = (lambda x: x - audio.size % x)(window_length_samples)
        song_input = np.pad(audio, (0, amount_to_pad))
        frequencies, _, stft = signal.stft(song_input,
                                            Fs, 
                                            nperseg=window_length_samples,  
                                            nfft=window_length_samples, 
                                            return_onesided=True)

        for time_index, window in enumerate(stft.T):
            
            spectrum = abs(window)

            # Encuentra las frecuencias mas importantes en la ventana
            peaks, props = signal.find_peaks(spectrum, prominence=0, distance=200)
            n_peaks = min(num_peaks, len(peaks))

            # Filtra las n frecuencias mas importantes
            largest_peaks = np.argpartition(props["prominences"], -n_peaks)[-n_peaks:]

            constellation_map += [[time_index, frequencies[peak]] for peak in peaks[largest_peaks]]

        return constellation_map

    @classmethod
    def create_hashes(cls, constellation_map, id_song=None):

        # Los hash se crean mediante una funcion de combinatoria
        hashes = {}

        for index, (time, freq) in enumerate(constellation_map):
            for other_time, other_freq in constellation_map[index : index + 100]: 

                diff = other_time - time

                if not 1 <= diff < 10:
                    continue

                hash = cls.freq_to_hash(freq, other_freq, diff)
                hashes[hash] = (time, id_song)

        return hashes

    @classmethod
    def freq_to_hash(freq, other_freq, diff, freq_upper=23_000, freq_bits=10):

        freq_binned = freq / freq_upper * (2 ** freq_bits)
        other_freq_binned = other_freq / freq_upper * (2 ** freq_bits)
        
        #crea un hash de 32 bits
        return int(freq_binned) | (int(other_freq_binned) << 10) | (int(diff) << 20)
