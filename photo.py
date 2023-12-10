from file_organizer import FileOrganizer


# organize photos
photo_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.raw']
photo_organizer = FileOrganizer('path/to/your/directory', 'PhotoFiles', photo_extensions)
photo_organizer.organize_files()