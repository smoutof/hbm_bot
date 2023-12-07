import pyautogui
from Resources import funcs


# Main loop
def main():
    while True:
        current_x, current_y = pyautogui.position() # Get current mouse x, y positions
        current_color = funcs.get_pixel_color(current_x, current_y) # Get current color of pixel from current x, y
        if current_color == (75, 219, 106): # If the color is green
            funcs.click(current_x, current_y) # Click


main()