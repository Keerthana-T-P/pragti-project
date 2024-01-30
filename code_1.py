import os
import pyttsx3
from PIL import ImageGrab
import pytesseract
import cv2
import time
import keyboard
import pygetwindow as gw

engine = pyttsx3.init()
engine.setProperty('rate', 200)
tesseract_path = r'C:\Users\tpgop\AppData\Local\Programs\Tesseract-OCR'
pytesseract.pytesseract.tesseract_cmd = os.path.join(tesseract_path, 'tesseract.exe')
nc_images_path = os.path.join(tesseract_path, 'NC_IMAGES')

def read_text(selected_region):
    try:
        text = pytesseract.image_to_string(selected_region)
        print("Detected Text: ", text)
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Error during text-to-speech:", e)
def capture_and_read_specific_region():
    if not os.path.exists(nc_images_path):
        os.makedirs(nc_images_path)
    time.sleep(3)
    active_window = gw.getActiveWindow()
    if active_window is not None:
        region_left = 600
        region_top = active_window.height - 52 - 850
        region_width = 720
        region_height = 890

        selected_region = (
            active_window.left + region_left,
            active_window.top + region_top,
            active_window.left + region_left + region_width,
            active_window.top + region_top + region_height
        )

        screenshot_path = os.path.join(nc_images_path, f"screenshot_{len(os.listdir(nc_images_path)) + 1}.png")
        screenshot = ImageGrab.grab(bbox=selected_region) # type: ignore
        screenshot.save(screenshot_path)

        screenshot = cv2.imread(screenshot_path)
        read_text(screenshot)


if __name__ == "__main__":
    print("Narrative cursor: Text to speech")
    input("Press enter to start capturing and reading specific region in the active window")
    while True:
        time.sleep(1)
        keyboard.press_and_release("enter")
        print("Capturing and reading specific region...")
        time.sleep(1)
        capture_and_read_specific_region()
        print("Processing complete")

