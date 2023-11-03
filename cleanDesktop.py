import os
import shutil

# Source folder (desktop path)
source_folder = r'C:\Users\pc\Desktop'

# Function to classify files and move them to appropriate folders
def classify_files(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.lnk':
        print(f"Skipping {file_path} (Shortcut file)...")
        return
    destination_folder = os.path.join(source_folder, file_extension[1:])  # Extract the file extension without the dot
    if file_extension == '.ini':
        print(f"Skipping {file_extension} (INI file)...")
        return
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)  # Create the folder if it doesn't exist
    shutil.move(file_path, destination_folder)
    print(f"Moved {file_path} to {destination_folder}")

# Main function to classify files on the desktop
def main():
    print("Classifying files on the desktop...")
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            classify_files(file_path)
    print("Classification completed.")

if __name__ == "__main__":
    main()
