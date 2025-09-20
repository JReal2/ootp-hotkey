# OOTP Hotkey Assistant

This script provides hotkeys to automate common actions in Out of the Park Baseball (OOTP).

- **F8**: Auto-play until tomorrow.
- **F9**: Save the game.
- **F12**: Stop the script.

## Requirements

- Anaconda or Miniconda
- OOTP Baseball running in **windowed mode** for best results.

## Setup

This is a one-time setup process.

1.  **Create Conda Environment:**
    Open the "Anaconda Prompt" (or a regular command prompt) and run the following command to create a dedicated environment for this script:
    ```
    conda create -n ootp python=3.9 -y
    ```

2.  **Install Dependencies:**
    Navigate to this project folder (`ootp_hotkey`) in your command prompt. Then, run the following command to install the required libraries into your new `ootp` environment:
    ```
    conda run -n ootp pip install -r requirements.txt
    ```

3.  **Configure Images:**
    This is the most important step. The script finds buttons by looking for images. You must replace the placeholder images in this folder with screenshots from your own game.
    - `autoplay.png`: A screenshot of the "auto-play until tomorrow" button.
    - `file.png`: A screenshot of the "File" menu button.
    - `save.png`: A screenshot of the "Save Game" button from the dropdown menu.

    **Important:** The screenshots should be small and tightly cropped around the button itself.

## Usage

After completing the one-time setup:

- Double-click `run_hotkeys.bat` to start the script.
- A command window will appear and the script will be running in the background.
- Start OOTP and use the F8 and F9 keys.
- To stop the script, press F12.