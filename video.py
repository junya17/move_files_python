from file_organizer import FileOrganizer


# organize videos
video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.mpeg', '.mpg', '.drt']
video_organizer = FileOrganizer('path/to/your/directory', 'VideoFiles', video_extensions)
video_organizer.organize_files()

