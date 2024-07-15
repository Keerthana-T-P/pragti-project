
# Narrative Cursor: Text-to-Speech

## Overview
This script captures a specific region of the active window, extracts text from the screenshot using Tesseract OCR, and converts it to speech using the `pyttsx3` library.

## Requirements
- Python 3.x
- Tesseract OCR (installed at `C:\Users\tpgop\AppData\Local\Programs\Tesseract-OCR`)
- Libraries: `pyttsx3`, `PIL`, `pytesseract`, `cv2`, `time`, `keyboard`, `pygetwindow`

## Usage
1. Install Tesseract OCR and set the path in the script.
2. Run the script (`python your_script_name.py`).
3. Press Enter to start capturing and reading the specific region.
4. The captured text will be read aloud.

## Notes
- Adjust the region coordinates (`region_left`, `region_top`, `region_width`, `region_height`) as needed.
- Ensure the active window is visible and contains the desired text.
- Customize the text-to-speech rate (`engine.setProperty('rate', 200)`).


Feel free to enhance this README with additional details or instructions specific to your use case. If you have any questions, let me know! 😊
