import os
import shutil
from pathlib import Path
import sys

# add project root to the python path
project_root = Path(__file__).resolve().parent
sys.path.append(str(project_root))
print(f"Added {project_root} to the python path.")

# Define your source and destination folder paths
source_folder_path = 'Complextext2animation/dataset/kit-mocap'
destination_folder_path = 'datasets/kit'

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder_path):
    os.makedirs(destination_folder_path)

# Define the file extensions to be moved
file_extensions = ["_meta.json", "_annotations.json", "_fke.csv"]

# Iterate over files in the source folder
for file in os.listdir(source_folder_path):
    # Check if the file ends with one of the specified extensions
    if any(file.endswith(ext) for ext in file_extensions):
        # Construct full file paths
        source_file = os.path.join(source_folder_path, file)
        destination_file = os.path.join(destination_folder_path, file)

        # Move the file
        shutil.move(source_file, destination_file)
        print(f"Moved: {file}")

print("File transfer complete.")
