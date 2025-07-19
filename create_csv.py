# create_csv.py

import os
import pandas as pd
from config import RAVDESS_DATA_FOLDER

print(f"Starting CSV creation for RAVDESS dataset...")
print(f"Looking for data in: {RAVDESS_DATA_FOLDER}")

# Check if the directory exists
if not os.path.isdir(RAVDESS_DATA_FOLDER):
    print(f"Error: The directory '{RAVDESS_DATA_FOLDER}' was not found.")
    print("Please make sure the path in config.py is correct and the folder exists.")
else:
    # This dictionary maps the emotion codes in the RAVDESS filenames to emotion names
    emotion_map = {
        '01': 'neutral',
        '02': 'calm',
        '03': 'happy',
        '04': 'sad',
        '05': 'angry',
        '06': 'fearful',
        '07': 'disgust',
        '08': 'surprised'
    }
    
    file_paths = []
    labels = []
    
    # Walk through the directory to find all .wav files
    for dirpath, dirnames, filenames in os.walk(RAVDESS_DATA_FOLDER):
        for filename in filenames:
            if filename.endswith('.wav'):
                # Filename example: 03-01-03-02-01-01-12.wav
                # The 3rd part (index 2) is the emotion code
                parts = filename.split('-')
                if len(parts) > 2:
                    emotion_code = parts[2]
                    if emotion_code in emotion_map:
                        # Get the full path to the audio file
                        full_path = os.path.join(dirpath, filename)
                        file_paths.append(full_path)
                        labels.append(emotion_map[emotion_code])

    if not file_paths:
        print("Error: No .wav files were found in the specified directory.")
        print("Please check that the RAVDESS dataset is correctly unzipped in the folder.")
    else:
        # Create a pandas DataFrame
        data_df = pd.DataFrame({
            'path': file_paths,
            'label': labels,
            'source': 'RAVDESS' # Adding the source column as expected by the project
        })
        
        # Save the DataFrame to a CSV file
        output_path = 'RAVDESS_dataset.csv'
        data_df.to_csv(output_path, index=False)
        
        print(f"Successfully created {output_path} with {len(data_df)} entries.")