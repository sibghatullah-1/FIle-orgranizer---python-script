# 📂 Python File Organizer

A Python script that **automatically organizes your files** into folders based on file types. Works for images, documents, videos, audio, scripts, archives, and more.

## How It Works

1.  The script asks you to enter the **path of the folder** you want to organize. format = "path/to/your/folder"
2.  It scans all files in the folder.
3.  For each file, it checks its **extension** and **moves it** into a corresponding folder (creating the folder if it doesn’t exist).
4.  Files with **unrecognized extensions** are left in place.

## Supported Categories

| Category | File Extensions |
| :--- | :--- |
| **Images** | `jpg`, `jpeg`, `png`, `gif`, `bmp`, `tiff`, `svg`, `webp` |
| **Documents** | `pdf`, `txt`, `docx`, `pptx`, `xls`, `xlsx`, `csv`, `odt`, `ods`, `rtf` |
| **Audio** | `mp3`, `wav`, `flac`, `aac`, `ogg` |
| **Video** | `mp4`, `avi`, `mkv`, `mov`, `wmv`, `flv` |
| **Scripts** | `py`, `java`, `c`, `cpp`, `js`, `html`, `css` |
| **Executables / Installers** | `exe`, `msi`, `apk`, `dmg` |
| **Compressed / Archives** | `zip`, `rar`, `7z`, `iso` |
| **Others** | Any file not listed above (will remain in the original folder) |

## 🚀 Usage

1.  Make sure **Python 3** is installed.
2.  **Save the script** as `file_organizer.py`.
3.  **Run the script** from your terminal:

    ```bash
    python file_organizer.py
    ```

4.  Enter the **full path of the folder** you want to organize when prompted.

### Path Format Examples:

* **Windows:** `C:\Users\YourName\Downloads\FolderToOrganize`
* **Mac / Linux:** `/home/username/Downloads/FolderToOrganize`

The script will organize your files and print a summary of file counts.

## ✨ Customization

* **Add or modify supported file types** by editing the `if-elif` sections in the script.
* **Change folder names** in the `folder_maker_and_mover` function calls.

## ⚠️ Notes

* Make sure the folder path exists and you have **permission to modify its contents**.
* The script **moves files**, so they will no longer remain in their original location.
