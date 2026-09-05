import subprocess
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InvalidSessionIdException

from pathlib import Path
import sys

import pyautogui





CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
DEBUG_PORT = 9222
USER_DATA_DIR = r"C:\temp\chrome-selenium"

BASE_DIR = Path(__file__).resolve().parent
JS_FILE = BASE_DIR / "ad.js"



def start_chrome():
    subprocess.Popen([
        CHROME_PATH,
        f"--remote-debugging-port={DEBUG_PORT}",
        f"--user-data-dir={USER_DATA_DIR}",
        "https://www.youtube.com"
    ])

    time.sleep(3)


def connect_selenium():
    options = Options()
    options.add_experimental_option(
        "debuggerAddress",
        f"127.0.0.1:{DEBUG_PORT}"
    )

    return webdriver.Chrome(options=options)


def load_js(filename):
    if getattr(sys, "frozen", False):
        base_dir = Path(sys._MEIPASS)
    else:
        base_dir = Path(__file__).resolve().parent

    js_file = base_dir / filename

    with open(js_file, "r", encoding="utf-8") as file:
        return file.read()

def adRunning(driver):
    js_code = load_js("ad.js")
    result = driver.execute_script(js_code)

    print("JS RESULT:", result)
    print("JS TYPE:", type(result))

    return result

def skipButtonExists(driver):
    js_code = load_js("skip.js")
    result = driver.execute_script(js_code)

    return bool(result)

def updateData(driver):
    return {
        "adRunning": adRunning(driver),
        "skipButton": skipButtonExists(driver),
        "skipButtonPosition": getSkipButtonPosition(driver)
    }

def getSkipButtonPosition(driver):
    js_code = load_js("btnPosition.js")
    result = driver.execute_script(js_code)

    if not result:
        return None

    # Position des Chrome-Fensters auf dem Windows-Desktop
    window_pos = driver.get_window_position()

    return {
        "x": window_pos["x"] + result["x"] + result["offset_x"],
        "y": window_pos["y"] + result["y"] + result["offset_y"],
        "width": result["width"],
        "height": result["height"],
        "center_x": window_pos["x"] + result["center_x"] + result["offset_x"],
        "center_y": window_pos["y"] + result["center_y"] + result["offset_y"]
    }

def getMousePosition():
    x, y = pyautogui.position()
    return {
        "x": x,
        "y": y
    }


def main():

    while True:
        data = updateData(driver)
        print(data)
        
        if data["adRunning"] and data["skipButton"] and data["skipButtonPosition"]:
            previousPos = getMousePosition()
            pyautogui.click(data["skipButtonPosition"]["center_x"], data["skipButtonPosition"]["center_y"])
            pyautogui.moveTo(previousPos["x"], previousPos["y"])
        
        time.sleep(1)
        
        
if __name__ == "__main__":
    try:
        start_chrome()
        driver = connect_selenium()
        print("Chrome Verbunden")
        
        main()
        
    except InvalidSessionIdException:
        print("\033[91m" + "Browser Closed" + "\033[0m")
        
    
    except Exception:
        driver.execute_script('alert("Error: Autoskip disabled"')
        

