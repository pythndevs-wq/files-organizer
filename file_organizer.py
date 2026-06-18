import shutil
from pathlib import Path


# ----------------------------
# File type rules (extension → folder mapping)
# This decides where each file will go
# ----------------------------
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css"]
}


# ----------------------------
# Moves a single file to its correct folder
# Also sends update to GUI log
# ----------------------------
def move_files(file, folder, base_path, log):

    # create final destination path
    destination = (base_path / folder) / file.name

    # move file to new location
    shutil.move(file, destination)

    # update GUI about move
    log(f"[✓] {file.name} → {folder}")


# ----------------------------
# Processes one folder (Downloads/Desktop/etc.)
# Scans all files and organizes them
# ----------------------------
def file_process(path, log):

    # notify that scanning started
    log(f"Opening: {path}")

    # loop through everything inside folder
    for item in path.iterdir():

        # only process files (ignore folders)
        if item.is_file():

            # check file type and match with rules
            for folder, extensions in file_types.items():

                if item.suffix.lower() in extensions:

                    # create folder if it doesn't exist
                    (path / folder).mkdir(exist_ok=True)

                    # move file + log it
                    move_files(item, folder, path, log)

                    break
                