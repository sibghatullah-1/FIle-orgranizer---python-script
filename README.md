File Organizer

A simple and clean Python script that automatically organizes files in a folder by sorting them into categorized subfolders based on their file extensions.

How It Works

The script scans the target directory, identifies each file's extension, and moves it into a corresponding folder. If the folder does not exist, the script creates it automatically.

For example:

.jpg, .png → Images

.pdf, .docx → Documents

.mp4, .mkv → Videos

.zip, .rar → Compressed

Any other extension will be placed in an Others folder

Usage Instructions
1. Set Your Folder Path

Open the script and modify this line:

org_folder_path = "path/to/your/folder"

Replace the value with the folder you want to organize.

2. Run the Script

Open a terminal in the script's directory and run:

python file_organizer.py

The script will:

Create required folders

Move files to their respective folders

3. Organize Again Anytime

You can re-run the script anytime to keep your folder tidy.

Script Structure

folder_maker_and_mover()

Creates a folder (if missing) and moves the file into it.

Main Logic

Reads all files from the target folder

Classifies each file by extension

Sorts them into the proper folder

Notes

Only files in the main directory are organized (subfolders are ignored).

System and hidden files are skipped.

Ensure the script has permission to create and move files.

License

You are free to use, modify, and share this project.
