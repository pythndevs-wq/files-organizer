from pathlib import Path
import shutil

print("Your Downloads are going to be managed")

path = Path.home() / "Downloads"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".m4a"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".xz"],
    "Code": [".py", ".c", ".cpp", ".js", ".html", ".css"],
    "Disk Images": [".iso"],
    "Programs": [".exe", ".deb"],
    "Apps": [".apk", ".xapk"]
}

if path.exists():
    print("Directory Opened")


def move_files(File, Folder):

    source = File
    destination = Path(path / Folder) / source.name

    shutil.move(source, destination)
    print(File, "Succesfully Moved to", {Folder})



for item in path.iterdir():

    if item.is_file:

        for folder, extensions in file_types.items():

            if item.suffix.lower() in extensions:

                Path(path / folder).mkdir(exist_ok=True)
                
                move_files(item, folder)

                break
                



