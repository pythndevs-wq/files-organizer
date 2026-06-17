import tkinter as tk
from download_m import file_process
from pathlib import Path

# ----------------------------
# Create main application window
# ----------------------------
root = tk.Tk()
root.geometry("500x500")
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


# ----------------------------
# Start the GUI event loop
# Keeps window running and responsive
# ----------------------------
root.mainloop()