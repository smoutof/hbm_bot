import pyautogui
import time

def get_pixel_color(x, y):
    return pyautogui.pixel(x, y)

def click(x, y):
    pyautogui.click(x=x, y=y)

def main():
    while True:
        current_color = get_pixel_color(550, 350)
        if current_color == (75, 219, 106):
            click(550, 350)

try:
    main()
except Exception as e:
    print(f'Unexpected error: {str(e)}')
    time.sleep(10000)