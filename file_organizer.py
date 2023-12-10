import os
import shutil


class FileOrganizer:
    def __init__(self, watch_folder, new_folder_name, file_extensions):
        self.watch_folder = watch_folder
        self.new_folder = new_folder_name
        self.file_extensions = file_extensions
        self.new_folder_path = os.path.join(self.watch_folder, self.new_folder)
        self.create_new_folder()

    def create_new_folder(self):
        try:
            if not os.path.exists(self.new_folder_path):
                os.makedirs(self.new_folder_path)
        except OSError as e:
            print(f"Error: Failed to create folder '{self.new_folder}'. Error message: {e}")

    def organize_files(self):
        for filename in os.listdir(self.watch_folder):
            if any(filename.lower().endswith(ext) for ext in self.file_extensions):
                source_path = os.path.join(self.watch_folder, filename)
                destination_path = os.path.join(self.new_folder_path, filename)
                try:
                    shutil.move(source_path, destination_path)
                    print(f"Moved file: {filename}")
                except Exception as e:
                    print(f"Error: Failed to move file '{filename}'. Error message: {e}")
        print("File movement completed.")
