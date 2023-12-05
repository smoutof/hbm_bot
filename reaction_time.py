import pyautogui

def get_pixel_color(x, y):
    return pyautogui.pixel(x, y)

def click(x, y):
    pyautogui.click(x=x, y=y)

def main():
    while True:
        current_x, current_y = pyautogui.position()
        current_color = get_pixel_color(current_x, current_y)
        if current_color == (75, 219, 106):
            click(current_x, current_y)

main()