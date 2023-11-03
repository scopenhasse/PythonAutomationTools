import os
import shutil
import time

# Source folder where downloaded files are located
source_folder = r'C:\Users\pc\Downloads'

# Destination folders for different file types
pdf_folder = r'C:\Users\pc\Downloads\pdfs'
images_folder = r'C:\Users\pc\Downloads\Images'
zip_folder = r'C:\Users\pc\Downloads\zips'
exe_folder = r'C:\Users\pc\Downloads\exes'

# Function to classify files
def classify_files(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.pdf':
        shutil.move(file_path, pdf_folder)
        print(f"Moved {file_path} to PDF folder")
    elif file_extension == '.jpg' or file_extension == '.jpeg' or file_extension == '.png':
        shutil.move(file_path, images_folder)
        print(f"Moved {file_path} to Images folder")
    elif file_extension == '.zip' or file_extension == '.rar':
        shutil.move(file_path, zip_folder)
        print(f"Moved {file_path} to ZIP folder")
    elif file_extension == '.exe':
        shutil.move(file_path, exe_folder)
        print(f"Moved {file_path} to EXE folder")
    elif file_extension == '.ini':
        print(f"Skipping {file_extension} Looking for new donwloads...")
    else:
        print(f"Unsupported file type: {file_extension}, skipping.")

# Main function to monitor the folder and classify files
def main():
    print("Monitoring the folder for new downloads...")
    while True:
        for filename in os.listdir(source_folder):
            file_path = os.path.join(source_folder, filename)
            if os.path.isfile(file_path):
                classify_files(file_path)
        time.sleep(10)  # Check for new files every 10 seconds

if __name__ == "__main__":
    main()
