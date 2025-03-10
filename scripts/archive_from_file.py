import csv
import os
import zipfile

def get_desktop_path():
    return os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def create_zip_from_directories(csv_file, archive_path):
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        with open(csv_file, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) > 1:
                    nam = row[0]
                    directory = row[1]
                    if os.path.isdir(directory):
                        for root, _, files in os.walk(directory):
                            for file in files:
                                if 'Cox' in file:
                                    file_path = os.path.join(root, file)
                                    zipf.write(file_path, nam + '\\' + os.path.relpath(file_path, directory))
                else:
                    print(f"Skipping row {row} as it does not have enough columns.")

if __name__ == "__main__":
    csv_file = 'data/cox_directories.csv'  # Replace with your CSV file path
    archive_path = get_desktop_path() + '/cox_archive.zip'  # Replace with your desired output zip file name
    create_zip_from_directories(csv_file, archive_path)
