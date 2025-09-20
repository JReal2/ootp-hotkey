# OOTP Hotkey Assistant

This script provides hotkeys to automate common actions in Out of the Park Baseball (OOTP).

- **F8**: Auto-play until tomorrow.
- **F9**: Save the game.
- **F12**: Stop the script.

## Requirements

- Python 3
- OOTP Baseball running in **windowed mode** for best results.

## Setup

1.  **Install Python:** If you don't have it, install Python 3 from [python.org](https://www.python.org/). Make sure to check "Add Python to PATH" during installation.

2.  **Install Dependencies:** Double-click on `run_hotkeys.bat`. It will automatically install the required libraries for you. If that fails, open a command prompt in this folder and run:
    ```
    pip install -r requirements.txt
    ```

3.  **Configure Images:** This is the most important step. The script finds buttons by looking for images. You must replace the placeholder images in this folder with screenshots from your own game.
    - `autoplay.png`: A screenshot of the "auto-play until tomorrow" button.
    - `file.png`: A screenshot of the "File" menu button.
    - `save.png`: A screenshot of the "Save Game" button from the dropdown menu.

    **Important:** The screenshots should be small and tightly cropped around the button itself.

## Usage

- Double-click `run_hotkeys.bat` to start the script.
- A command window will appear. You can minimize it, but do not close it.
- Start OOTP and use the F8 and F9 keys.
- To stop the script, press F12 or close the command window.

## Troubleshooting

### 'python' is not recognized Error

When you run `run_hotkeys.bat`, you might see an error that says `python` is not recognized. This means that Python is either not installed, or its location is not in your system's PATH.

To fix this, you need to tell the script exactly where your Python is installed.

1.  **Find your `python.exe` path:**
    - Open a Command Prompt (`cmd.exe`).
    - Type `where python`. This should print a path, for example `C:\Users\YourName\AppData\Local\Programs\Python\Python39\python.exe`.
    - Copy this path.

2.  **Edit `run_hotkeys.bat`:**
    - Right-click on `run_hotkeys.bat` and choose "Edit" (or open it with Notepad).
    - Find this line:
      ```batch
      start /b "" python ootp_hotkey.py
      ```
    - Replace `python` with the full path to your python executable, wrapped in quotes. For example:
      ```batch
      start /b "" "C:\Users\YourName\AppData\Local\Programs\Python\Python39\python.exe" ootp_hotkey.py
      ```
    - Save the file and run it again.
