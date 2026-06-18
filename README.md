# 📂 Downloads Organizer

A simple Python automation tool that organizes files from multiple folders (Downloads, Desktop, Documents, etc.) into categorized folders based on file type.

---

## 🚀 Features

- Works on **Linux & Windows**
- Organizes multiple default folders automatically
- Sorts files by extension:
  - Images
  - Videos
  - Audio
  - Documents
  - Archives
  - Code
  - Apps / Programs
- Automatically creates required folders
- Safe skipping for missing directories
- Case-insensitive extension handling

---

## 📁 Supported Paths

The script scans:

- Downloads
- Desktop
- Documents
- Pictures
- Videos
- Music

(All based on `Path.home()` → cross-platform safe)

---

## 🛠️ Requirements

- Python 3.x

No external libraries needed (uses built-in modules only):
- pathlib
- shutil

---

## ▶️ How to Run

```bash
python organizer.py