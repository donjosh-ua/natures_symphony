from pickle import load
import json
from scipy.io.wavfile import read
import controller.fingerprint as fngp


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

def find_animal(audio_input, Fs):

    try:
        database = load(open('database.dat', 'rb'))
        audio_name_index = load(open('audio_index.dat', 'rb'))
    except FileNotFoundError:
        print("Database or audio index file not found.")
        return []
    
    constellation = fngp.create_constellation(audio_input, Fs)
    hashes = fngp.create_hashes(constellation, None)
    scores = score_hashes_against_database(hashes, database)
    total_score = sum(score[1][1] for score in scores)

    if total_score == 0:
        return [("No matches found", 1.0)]

    return get_animal_info(scores[0][0])

def get_animal_info(animal_name):

    # Load the JSON data
    with open('./animals.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Search for the animal
    for animal in data['animals']:
        if animal['nombre'].lower() == animal_name.lower():
            return animal
    
    # If no animal is found
    return None


def print_matches(file_name, num_matches=1):
    
    try:
        database = load(open('database.dat', 'rb'))
        audio_name_index = load(open('audio_index.dat', 'rb'))
    except FileNotFoundError:
        pass

    Fs, audio_input = read(file_name)
    constellation = fngp.create_constellation(audio_input, Fs)
    hashes = fngp.create_hashes(constellation, None)

    scores = score_hashes_against_database(hashes, database)[:num_matches]
    print(f'Audio con mayor parecido\n{audio_name_index[scores.pop(0)[0]].split("/")[-1]}')
    if num_matches == 1:
        return
    
    print('Otras coincidencias')
    for audio_id, _ in scores:
        print(f"{audio_name_index[audio_id].split('/')[-1]}")