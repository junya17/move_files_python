from file_organizer import FileOrganizer


# organize photos
photo_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.raw']
photo_organizer = FileOrganizer('path/to/your/directory', 'PhotoFiles', photo_extensions)
photo_organizer.organize_files()

# organize videos
video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.mpeg', '.mpg', '.drt']
video_organizer = FileOrganizer('path/to/your/directory', 'VideoFiles', video_extensions)
video_organizer.organize_files()

# organize music files
music_extensions = ['.mp3', '.wav', '.aac', '.flac', '.m4a', '.ogg', '.wma', '.midi', '.mid']
music_organizer = FileOrganizer('path/to/your/directory', 'MusicFiles', music_extensions)
music_organizer.organize_files()

# path/to/your/directory