import csv
import os
import zipfile
from tqdm import tqdm

def get_desktop_path():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def zip_directories_with_string(parent_directory, search_terms, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
          # Count total files for progress bar
          total_files = sum(len(files) for _, _, files in os.walk(parent_directory))
          progress_bar = tqdm(total=total_files, desc="Zipping files", unit="file")
          with open(csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) > 1:
                    nam = row[0]
                    parent_directory = row[1]
                    if os.path.isdir(parent_directory):  
                        for root, dirs, files in os.walk(parent_directory):
                            # Check if the directory name contains the search term
                            if any(term in os.path.basename(root) for term in search_terms):
                                for dirpath, dirnames, filenames in os.walk(root):
                                    for filename in filenames:
                                        file_path = os.path.join(dirpath, filename)                                       
                                        zipf.write(file_path, nam + '\\' + os.path.relpath(file_path, parent_directory))      
                                        progress_bar.update(1)
                            for file in files:
                                # Check if any file name in the directory contains the search term
                                if 'bin' in parent_directory:
                                    if 'SMU.Cox' in file:
                                        file_path = os.path.join(root, file)
                                        zipf.write(file_path, nam + '\\' + os.path.relpath(file_path, parent_directory))     
                                        progress_bar.update(1)
                        progress_bar.close()
                else:
                    print(f"Skipping row {row} as it does not have enough columns.")
if __name__ == "__main__":
    search_terms = ['Cox', 'COX', 'cox']
    csv_file = 'data/cd02t.csv'  # Replace with your CSV file path
    archive_path = get_desktop_path() + '/cox_archive_cd02t.zip'  # Replace with your desired output zip file name
    zip_directories_with_string(csv_file,search_terms,archive_path)
