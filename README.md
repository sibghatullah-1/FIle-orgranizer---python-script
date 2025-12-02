# File Organizer

A simple and clean Python script that automatically organizes files in a folder by sorting them into categorized subfolders based on their file extensions.

## How It Works

The script scans the target directory, identifies each file's extension, and moves it into a corresponding folder. If the folder does not exist, the script creates it automatically.

For example:

* `.jpg`, `.png` → **Images**
* `.pdf`, `.docx` → **Documents**
* `.mp4`, `.mkv` → **Videos**
* `.zip`, `.rar` → **Compressed**
* Any other extension will be placed in an **Others** folder

---

## Usage Instructions

### 1. **Set Your Folder Path**

Open the script and modify this line:

```python
org_folder_path = "path/to/your/folder"
```

Replace the value with the folder you want to organize.

### 2. **Run the Script**

Open a terminal in the script's directory and run:

```bash
python file_organizer.py
```

The script will:

* Create required folders
* Move files to their respective folders

### 3. **Organize Again Anytime**

You can re-run the script anytime to keep your folder tidy.

---

## Script Structure

* **folder_maker_and_mover()**

  * Creates a folder (if missing) and moves the file into it.
* **Main Logic**

  * Reads all files from the target folder
  * Classifies each file by extension
  * Sorts them into the proper folder

---

## Notes

* Only files in the main directory are organized (subfolders are ignored).
* System and hidden files are skipped.
* Ensure the script has permission to create and move files.

---

## License

You are free to use, modify, and share this project.

---

If you want me to add formatting, badges, or installation steps, let me know!

### 3. **What Happens Next**

* The script scans all files in the chosen folder.
* It checks each file’s extension.
* It creates destination folders if needed.
* It moves the files into the correct category.

---

## Example Categories Used in the Script

You can modify or expand these categories in the code based on your needs:

* **Images**: jpg, jpeg, png, gif, svg
* **Documents**: pdf, txt, doc, docx, pptx, xlsx
* **Videos**: mp4, mkv, mov, avi
* **Compressed**: zip, rar, 7z, tar, gz
* **Others**: any file type not listed above

---

## Requirements

* Python 3.x
* No external libraries required

---

## Running the Script Automatically (Optional)

If you want this to run automatically (e.g., daily):

* Use **Task Scheduler** on Windows
* Use **Cron Jobs** on Linux/macOS

---

## Notes

* The script does not delete or modify file contents — it only moves them.
* Make sure no apps are using the files while organizing.

---

## License

This project is open-source and free to use.
