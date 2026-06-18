
import tkinter as tk
from file_organizer import file_process
from pathlib import Path

# ----------------------------
# Create main application window
# ----------------------------
root = tk.Tk()
root.geometry("500x700")
root.title("Smart File Organizer v1.0")
root.configure(bg="#1e1e2e")


# ----------------------------
# Text box for showing live logs
# (this is where we print progress)
# ----------------------------
log_box = tk.Text(root, height=15, width=50, bg="#111", fg="white")
log_box.pack(pady=20)


# ----------------------------
# Welcome message shown on UI
# ----------------------------
greet_label = tk.Label(
    root,
    text="Welcome 😈 Click to Organize Files",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="#1e1e2e"
)
greet_label.pack()


# ----------------------------
# Helper function to print logs
# instead of console print, we show inside GUI
# ----------------------------
def log(message):
    log_box.insert(tk.END, message + "\n")
    log_box.see(tk.END)  # auto scroll to latest message


# ----------------------------
# Main function that runs when button is clicked
# This connects GUI with backend logic
# ----------------------------
def start_organizing():
    # Clear previous logs
    log_box.delete("1.0", tk.END)

    log("Organizing started...\n")

    # List of default system folders to scan
    paths = [
        Path.home() / "Downloads",
        Path.home() / "Desktop",
        Path.home() / "Documents",
        Path.home() / "Pictures",
        Path.home() / "Videos",
        Path.home() / "Music",
    ]

    # Loop through each folder safely
    for path in paths:

        # Skip if folder doesn't exist on system
        if not path.exists():
            log(f"[SKIP] {path}")
            continue

        log(f"\nScanning: {path}")

        # Call backend function and pass log so it can update UI
        file_process(path, log)

    log("\nDone 😈")


def custom_path_organize():

    # Clear previous logs
    log_box.delete("1.0", tk.END)

    log("Organizing started...\n")

    custom_path = Path(path_entry.get())

    if not custom_path.exists():
        return log(f"[SKIP] {custom_path} (Path does not exist)")

    if not custom_path.is_dir():
        return log(f"[SKIP] {custom_path} (Not a folder)")

    log(f"\nScanning: {custom_path}")

    file_process(custom_path, log)

    log("\nDone 😈")

# ----------------------------
# Button to start the process
# User clicks this to begin organizing
# ----------------------------
btn = tk.Button(
    root,
    text="Order Chaos",
    command=start_organizing,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 14, "bold")
)
btn.pack(pady=10)

#----------------------------
# Label for alternative input
#----------------------------
or_label = tk.Label(root, text="Or\nEnter the path to organize:", font=("Arial", 12), fg="white", bg="#1e1e2e")
or_label.pack(pady=10)

path_entry = tk.Entry(root, width=40, bg="#111", fg="white")
path_entry.pack(pady=5)

#----------------------------
# Button for custom path organization
#----------------------------
custom_btn = tk.Button(
    root,
    text="Organize Custom Path",
    command=custom_path_organize,
    bg="#2196F3",
    fg="white",
    font=("Arial", 14, "bold")
)
custom_btn.pack(pady=10)


# ----------------------------
# Start the GUI event loop
# Keeps window running and responsive
# ----------------------------
root.mainloop()