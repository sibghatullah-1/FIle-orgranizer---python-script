import os
import shutil


def folder_maker_and_mover(folder_name, filename):
    folder_path = os.path.join(org_folder_path, folder_name)

    source = os.path.join(org_folder_path, filename)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    shutil.move(source, folder_path)


print(
    """                                                                                                                                                   
 ▄▄▄▄▄▄   ▀    ▀▀█                                                       ▀                                                       ▀             ▄   
 █      ▄▄▄      █     ▄▄▄           ▄▄▄    ▄ ▄▄   ▄▄▄▄   ▄▄▄   ▄ ▄▄   ▄▄▄    ▄▄▄▄▄   ▄▄▄    ▄ ▄▄          ▄▄▄    ▄▄▄    ▄ ▄▄  ▄▄▄    ▄▄▄▄   ▄▄█▄▄ 
 █▄▄▄▄▄   █      █    █▀  █         █▀ ▀█   █▀  ▀ █▀ ▀█  ▀   █  █▀  █    █       ▄▀  █▀  █   █▀  ▀        █   ▀  █▀  ▀   █▀  ▀   █    █▀ ▀█    █   
 █        █      █    █▀▀▀▀         █   █   █     █   █  ▄▀▀▀█  █   █    █     ▄▀    █▀▀▀▀   █             ▀▀▀▄  █       █       █    █   █    █   
 █      ▄▄█▄▄    ▀▄▄  ▀█▄▄▀         ▀█▄█▀   █     ▀█▄▀█  ▀▄▄▀█  █   █  ▄▄█▄▄  █▄▄▄▄  ▀█▄▄▀   █            ▀▄▄▄▀  ▀█▄▄▀   █     ▄▄█▄▄  ██▄█▀    ▀▄▄ 
                                                   ▄  █                                                                               █            
                                                    ▀▀                                                                                ▀            """
)


print(
    "This script will organize your jpg, jpeg, png, gif, bmp, tiff, svg, webp, "
    "pdf, txt, docx, pptx, xls, xlsx, csv, odt, ods, rtf, "
    "mp3, wav, flac, aac, ogg, "
    "mp4, avi, mkv, mov, wmv, flv, "
    "py, java, c, cpp, js, html, css, "
    "exe, msi, apk, dmg, "
    "zip, rar, 7z, iso "
    "files into separate folders.\n"
)


print(
    "-You just need to copy and paste the folder path in the section given below\nfor which you want to organize the files-"
)
print(" -----------------------------------------------------------")
print("|               Enter the folder path here                |")
print(" -----------------------------------------------------------")
folder_directory_by_user = input("Path: ")  # cursor appears normally below the box


folderlist = os.listdir(folder_directory_by_user)

org_folder_path = folder_directory_by_user
pdf = 0
jpg = 0
png = 0
txt = 0
mp4 = 0
pptx = 0
docx = 0
excel = 0
compressed = 0

# Newly added ones
gif = 0
bmp = 0
tiff = 0
svg = 0
webp = 0

mp3 = 0
wav = 0
flac = 0
aac = 0
ogg = 0

avi = 0
mkv = 0
mov = 0
wmv = 0
flv = 0

xls = 0
xlsx = 0
csv = 0
odt = 0
ods = 0
rtf = 0

py = 0
java = 0
c = 0
cpp = 0
js = 0
html = 0
css = 0

exe = 0
msi = 0
apk = 0
dmg = 0

iso = 0
rar = 0
z7 = 0  # for .7z

for i in folderlist:

    filename = i
    name, ext = os.path.splitext(filename)

    if ext == ".jpg" or ext == ".jpeg":
        folder_name = "jpeg files"

        folder_maker_and_mover(folder_name, i)
        print("It is a jped file")
        print(name + ext + "\n")
        jpg += 1
    elif ext == ".png":
        folder_name = "png files"
        folder_maker_and_mover(folder_name, i)

        print("it is a png file")
        print(name + ext + "\n")
        png += 1
    elif ext == ".mp4":
        folder_name = "mp4 files"
        folder_maker_and_mover(folder_name, i)

        print("it is a mp4 file")
        print(name + ext + "\n")
        mp4 += 1
    elif ext == ".pdf":
        folder_name = "pdf files"
        folder_maker_and_mover(folder_name, i)
        print("It is a pdf file")
        print(name + ext + "\n")
        pdf += 1
    elif ext == ".zip":
        folder_name = "compressed files"
        folder_maker_and_mover(folder_name, i)

        print("It is a compresed file")
        print(name + ext + "\n")
        compressed += 1

    elif ext == ".pptx":
        folder_name = "pptx files"
        folder_maker_and_mover(folder_name, i)

        print("It is a pptx file")
        print(name + ext + "\n")
        pptx += 1

    elif ext == ".txt":
        folder_name = "text files"
        folder_maker_and_mover(folder_name, i)

        print("It is a text file")
        print(name + ext + "\n")
        txt += 1
    elif ext == ".docx":
        folder_name = "docx and word files"
        folder_maker_and_mover(folder_name, i)

        print("It is a docx or word file")
        print(name + ext + "\n")
        docx += 1
    elif ext == ".gif":
        folder_name = "gif files"
        folder_maker_and_mover(folder_name, i)
        print("It is a gif file")
        print(name + ext + "\n")
        gif += 1

    elif ext == ".mp3":
        folder_name = "audio files"
        folder_maker_and_mover(folder_name, i)
        print("It is an mp3 file")
        print(name + ext + "\n")
        mp3 += 1

    elif ext == ".wav":
        folder_name = "audio files"
        folder_maker_and_mover(folder_name, i)
        print("It is a wav file")
        print(name + ext + "\n")
        wav += 1

    elif ext == ".mkv":
        folder_name = "video files"
        folder_maker_and_mover(folder_name, i)
        print("It is an mkv video file")
        print(name + ext + "\n")
        mkv += 1

    elif ext == ".xlsx" or ext == ".xls":
        folder_name = "excel files"
        folder_maker_and_mover(folder_name, i)
        print("It is an Excel file")
        print(name + ext + "\n")
        excel += 1

    elif ext == ".csv":
        folder_name = "csv files"
        folder_maker_and_mover(folder_name, i)
        print("It is a CSV file")
        print(name + ext + "\n")
        csv += 1

    elif ext == ".py":
        folder_name = "python scripts"
        folder_maker_and_mover(folder_name, i)
        print("It is a Python file")
        print(name + ext + "\n")
        py += 1

    elif ext == ".exe":
        folder_name = "executables"
        folder_maker_and_mover(folder_name, i)
        print("It is an EXE file")
        print(name + ext + "\n")
        exe += 1

    elif ext == ".rar" or ext == ".7z":
        folder_name = "compressed files"
        folder_maker_and_mover(folder_name, i)
        print("It is a compressed archive")
        print(name + ext + "\n")
        compressed += 1
    elif ext == ".py":
        folder_name = "python scripts"
        folder_maker_and_mover(folder_name, i)
        print("It is a Python file")
        print(name + ext + "\n")
        py += 1
    elif ext == ".bmp":
        folder_name = "bmp files"
        folder_maker_and_mover(folder_name, i)
        print("It is a BMP file")
        print(name + ext + "\n")
        bmp += 1

    elif ext == ".tiff":
        folder_name = "tiff files"
        folder_maker_and_mover(folder_name, i)
        print("It is a TIFF file")
        print(name + ext + "\n")
        tiff += 1

    elif ext == ".svg":
        folder_name = "svg files"
        folder_maker_and_mover(folder_name, i)
        print("It is an SVG file")
        print(name + ext + "\n")
        svg += 1

    elif ext == ".webp":
        folder_name = "webp files"
        folder_maker_and_mover(folder_name, i)
        print("It is a WEBP file")
        print(name + ext + "\n")
        webp += 1

    elif ext == ".flac":
        folder_name = "audio files"
        folder_maker_and_mover(folder_name, i)
        print("It is a FLAC file")
        print(name + ext + "\n")
        flac += 1

    elif ext == ".aac":
        folder_name = "audio files"
        folder_maker_and_mover(folder_name, i)
        print("It is an AAC file")
        print(name + ext + "\n")
        aac += 1

    elif ext == ".ogg":
        folder_name = "audio files"
        folder_maker_and_mover(folder_name, i)
        print("It is an OGG file")
        print(name + ext + "\n")
        ogg += 1

    elif ext == ".avi":
        folder_name = "video files"
        folder_maker_and_mover(folder_name, i)
        print("It is an AVI file")
        print(name + ext + "\n")
        avi += 1

    elif ext == ".mov":
        folder_name = "video files"
        folder_maker_and_mover(folder_name, i)
        print("It is a MOV file")
        print(name + ext + "\n")
        mov += 1

    elif ext == ".wmv":
        folder_name = "video files"
        folder_maker_and_mover(folder_name, i)
        print("It is a WMV file")
        print(name + ext + "\n")
        wmv += 1

    elif ext == ".flv":
        folder_name = "video files"
        folder_maker_and_mover(folder_name, i)
        print("It is an FLV file")
        print(name + ext + "\n")
        flv += 1

    elif ext == ".odt":
        folder_name = "odt files"
        folder_maker_and_mover(folder_name, i)
        print("It is an ODT file")
        print(name + ext + "\n")
        odt += 1

    elif ext == ".ods":
        folder_name = "ods files"
        folder_maker_and_mover(folder_name, i)
        print("It is an ODS file")
        print(name + ext + "\n")
        ods += 1

    elif ext == ".rtf":
        folder_name = "rtf files"
        folder_maker_and_mover(folder_name, i)
        print("It is an RTF file")
        print(name + ext + "\n")
        rtf += 1

    elif ext == ".java":
        folder_name = "java files"
        folder_maker_and_mover(folder_name, i)
        print("It is a Java file")
        print(name + ext + "\n")
        java += 1

    elif ext == ".c":
        folder_name = "c files"
        folder_maker_and_mover(folder_name, i)
        print("It is a C file")
        print(name + ext + "\n")
        c += 1

    elif ext == ".cpp":
        folder_name = "cpp files"
        folder_maker_and_mover(folder_name, i)
        print("It is a C++ file")
        print(name + ext + "\n")
        cpp += 1

    elif ext == ".js":
        folder_name = "javascript files"
        folder_maker_and_mover(folder_name, i)
        print("It is a JavaScript file")
        print(name + ext + "\n")
        js += 1

    elif ext == ".html":
        folder_name = "html files"
        folder_maker_and_mover(folder_name, i)
        print("It is an HTML file")
        print(name + ext + "\n")
        html += 1

    elif ext == ".css":
        folder_name = "css files"
        folder_maker_and_mover(folder_name, i)
        print("It is a CSS file")
        print(name + ext + "\n")
        css += 1

    elif ext == ".msi":
        folder_name = "installers"
        folder_maker_and_mover(folder_name, i)
        print("It is an MSI file")
        print(name + ext + "\n")
        msi += 1

    elif ext == ".apk":
        folder_name = "apk files"
        folder_maker_and_mover(folder_name, i)
        print("It is an APK file")
        print(name + ext + "\n")
        apk += 1

    elif ext == ".dmg":
        folder_name = "dmg files"
        folder_maker_and_mover(folder_name, i)
        print("It is a DMG file")
        print(name + ext + "\n")
        dmg += 1

    elif ext == ".iso":
        folder_name = "iso files"
        folder_maker_and_mover(folder_name, i)
        print("It is an ISO file")
        print(name + ext + "\n")
        iso += 1

    else:
        print("File type not recognized")
        print(name + ext + "\n")

print(
    f"The total pdf are {pdf}\nThe total jpgs are {jpg}\nThe total png are {png}\nThe total compressed are {compressed}\nThe total txt files are {txt}"
)
