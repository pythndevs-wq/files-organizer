# 📂 Smart File Organizer

Smart File Organizer is a Python desktop application that automatically organizes files into categorized folders based on their file extensions. It provides a simple graphical interface built with Tkinter and supports both automatic organization of common system folders and custom folder organization.

## Features

### Automatic Organization

Organize files from common user directories:

* Downloads
* Desktop
* Documents
* Pictures
* Videos
* Music

### Custom Folder Support

Enter any folder path and organize its contents directly from the application.

### Live Activity Log

Monitor file operations in real time through the built-in log window.

### File Categories

The application currently organizes files into:

* Images
* Videos
* Audio
* Documents
* Archives
* Code

### Cross-Platform Support

Designed to work on both:

* Linux
* Windows

## Technologies Used

* Python
* Tkinter
* pathlib
* shutil

No third-party dependencies are required.

## Project Structure

```text
Smart-File-Organizer/
│
├── main_gui.py          # Graphical user interface
├── file_organizer.py    # File organization logic
├── README.md
└── .gitignore
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/pythndevs-wq/downloads-organizer.git
cd downloads-organizer
```

Run the application:

```bash
python main_gui.py
```

## Usage

### Organize Default System Folders

Click the **Order Chaos** button to organize the default user directories.

### Organize a Custom Folder

1. Enter a folder path in the input field.
2. Click **Organize Custom Path**.
3. View progress in the live log area.

## Safety Features

* Checks whether a path exists before processing.
* Verifies that the provided path is a directory.
* Ignores unsupported file types.
* Creates destination folders automatically when needed.

## Learning Objectives

This project was created to practice:

* Python automation
* File handling
* GUI development with Tkinter
* Modular project structure
* Callback functions
* Working with pathlib

## Future Improvements

* Folder selection dialog
* Progress bar
* Multi-threading for smoother UI
* Undo functionality
* Configuration file support
* Windows executable builds
* Automated GitHub Actions workflow

## Author

**Zeeshan Afzal**

Self-learning Python developer exploring automation, computer science, and artificial intelligence.
