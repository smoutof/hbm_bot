import pyautogui

# Pixel color function using pyautogui
def get_pixel_color(x, y):
    return pyautogui.pixel(x, y)

# Click function using pyautogui
def click(x, y):
    pyautogui.click(x=x, y=y)

# Main loop
def main():
    while True:
        current_x, current_y = pyautogui.position() # Get current mouse x, y positions
        current_color = get_pixel_color(current_x, current_y) # Get current color of pixel from current x, y
        if current_color == (75, 219, 106): # If the color is green
            click(current_x, current_y) # Click


main()