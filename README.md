# 📂 Smart File Organizer v1.0

A Python-based automation tool with a graphical interface that organizes files from system folders into categorized directories.

---

## 🚀 Features

- Graphical User Interface (Tkinter)
- Live logging of file movements
- Modular backend design (GUI + logic separated)
- Organizes files by type:
  - Images
  - Videos
  - Audio
  - Documents
  - Archives
  - Code files
- Cross-platform support (Linux & Windows)
- Safe folder scanning with skip handling

---

## 🧠 How It Works

1. User clicks **"Order Chaos"**
2. Application scans default system folders:
   - Downloads
   - Desktop
   - Documents
   - Pictures
   - Videos
   - Music
3. Files are categorized based on extension
4. Files are moved into proper folders
5. Live logs are shown in GUI

---

## 🖥️ UI Features

- Dark themed interface
- Greeting message
- Start button
- Live log window showing real-time file actions

---

## 🛠️ Tech Used

- Python 3
- Tkinter (GUI)
- pathlib (file handling)
- shutil (file moving)

---

## 📁 Project Structure

```text
main_gui.py     → GUI layer
download_m.py   → backend logic (file processing)
