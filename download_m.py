#!/usr/bin/env python3

from pathlib import Path
import shutil

print("This will oigaize your whole Windows/Linux default folder's files")
input("Press enter to start")
print("Your Downloads are going to be managed")

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

paths = [
    Path.home() / "Downloads",
    Path.home() / "Desktop",
    Path.home() / "Documents",
    Path.home() / "Pictures",
    Path.home() / "Videos",
    Path.home() / "Music",
]


def move_files(file, folder, base_path):
    destination = (base_path / folder) / file.name
    shutil.move(file, destination)
    print(file.name, "Successfully moved to", folder)


def file_process(folder_path):

    if not folder_path.exists():
        return

    print("Directory Opened:", folder_path)

    for item in folder_path.iterdir():

        if item.is_file():

            for folder, extensions in file_types.items():

                if item.suffix.lower() in extensions:

                    (folder_path / folder).mkdir(exist_ok=True)

                    move_files(item, folder, folder_path)

                    break


for path in paths:
    file_process(path)