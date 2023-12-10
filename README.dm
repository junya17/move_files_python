# FileOrganizer

## Overview
The `FileOrganizer` is a Python script designed to automatically organize files on your desktop based on their file extensions. It efficiently manages files such as photos, music, and videos by moving them into specified directories.

## Features
- Organizes files into different folders based on their extensions.
- Customizable for various file types including photos, music, and video files.
- Automates file management to keep your desktop clean and organized.

## Requirements
- Python 3.x
- OS Module (Standard Library)
- SHUTIL Module (Standard Library)

## Setup
1. Clone or download the repository to your local machine.
2. Ensure Python 3.x is installed on your system.

## Configuration
Configure the following variables in the `FileOrganizer` class before running the script:
- `watch_folder`: The directory to be monitored (e.g., your Desktop).
- `new_folder`: The name of the folder where organized files will be moved.
- `file_extensions`: The list of file extensions to organize.

Example:
```python
photo_extensions = ['.jpg', '.jpeg', '.png', '.gif']
photo_organizer = FileOrganizer('/path/to/Desktop', 'PhotoFiles', photo_extensions)
