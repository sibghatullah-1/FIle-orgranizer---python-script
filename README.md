📂 Python File Organizer

Clean up your messy directories in seconds.

This is a lightweight Python automation script designed to organize files within a specific folder. It scans the directory, detects file types based on extensions, creates appropriate subfolders (if they don't exist), and moves the files into their respective categories.

🧐 Why use this?

If your Downloads or Desktop folder looks like a chaotic mix of images, installers, documents, and random zips, this script is the solution.

Before:

/Downloads
  ├── receipt.pdf
  ├── holiday.jpg
  ├── setup.exe
  ├── meme.png
  └── homework.docx


After:

/Downloads
  ├── /pdf files
  │     └── receipt.pdf
  ├── /jpeg files
  │     └── holiday.jpg
  ├── /executables
  │     └── setup.exe
  ├── /png files
  │     └── meme.png
  └── /docx and word files
        └── homework.docx


🚀 How to Run

Prerequisites

You need Python 3.x installed on your system.

Step-by-Step Usage

Download the script Save the python file (e.g., organizer.py) to your computer.

Open your Terminal or Command Prompt Navigate to the location where you saved the script.

Run the command ```bash
python organizer.py




Enter the Target Path The script will display a welcome banner and ask for a path:

 -----------------------------------------------------------
|               Enter the folder path here                |
 -----------------------------------------------------------
Path: 


Paste the absolute path of the folder you want to clean up.

Windows Example: C:\Users\YourName\Downloads

Mac/Linux Example: /Users/YourName/Downloads

Done! The script will log every file it moves and provide a summary count at the end.

🗂️ Supported File Formats

The script automatically recognizes and sorts the following formats into these categories:

Category

Extensions

Images

.jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg, .webp

Videos

.mp4, .avi, .mkv, .mov, .wmv, .flv

Audio

.mp3, .wav, .flac, .aac, .ogg

Documents

.pdf, .txt, .docx, .pptx, .xls, .xlsx, .csv, .odt, .ods, .rtf

Coding/Web

.py, .java, .c, .cpp, .js, .html, .css

Installers

.exe, .msi, .apk, .dmg

Archives

.zip, .rar, .7z, .iso

Note: Files with extensions not listed above will be skipped and left in the main directory.

⚙️ How it Works (Under the Hood)

Input: Accepts a directory path from the user.

Iteration: Loops through every file in that directory.

Extraction: splits the filename to get the extension (e.g., .png).

Decision: Checks the extension against a list of known types.

Action: - Checks if the destination folder exists (e.g., png files).

If not, it creates it using os.mkdir.

Moves the file into that folder using shutil.move.

⚠️ Disclaimer

Always ensure you have a backup of important data before running automation scripts on your files. While this script is safe, file operations should always be done with care.
