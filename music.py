from file_organizer import FileOrganizer


# organize music files
music_extensions = ['.mp3', '.wav', '.aac', '.flac', '.m4a', '.ogg', '.wma', '.midi', '.mid']
music_organizer = FileOrganizer('path/to/your/directory', 'MusicFiles', music_extensions)
music_organizer.organize_files()

