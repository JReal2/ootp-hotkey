# OOTP Hotkey Assistant

This script provides hotkeys to automate common actions in Out of the Park Baseball (OOTP).

- **F8**: Auto-play until tomorrow.
- **F9**: Save the game.
- **F10**: View yesterday's Box Score.
- **Ctrl+Q**: Stop the script.

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
    - `yesterday.png`: A screenshot of the "YESTERDAY" text that appears on the home screen after a game is played.

    **Important:** The screenshots should be small and tightly cropped around the element itself.

## Usage

After completing the one-time setup:

- Double-click `run_hotkeys.bat` to start the script.
- A command window will appear and the script will be running in the background.
- Start OOTP and use the F8, F9, and F10 keys.
- To stop the script, press Ctrl+Q.

## Fine-Tuning (Optional)

If the F10 key doesn't click the Box Score button correctly, you may need to adjust the click position.

1. Open the `ootp_hotkey.py` file in a text editor.
2. Find these lines at the top of the file:
   ```python
   BOX_SCORE_OFFSET_X = 150 # X축으로 150픽셀 오른쪽으로 이동
   BOX_SCORE_OFFSET_Y = 0   # Y축 이동은 없음
   ```
3. Adjust the `BOX_SCORE_OFFSET_X` value. If the script clicks too far to the right, decrease the number. If it clicks too far to the left, increase it. You can also adjust `BOX_SCORE_OFFSET_Y` for vertical position.
4. Save the file and restart the `run_hotkeys.bat` script to apply the changes.
