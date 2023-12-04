import pyautogui
import time

# Define specific pixel locations to monitor
pixel_locations = [(820, 350), (950, 350), (1100, 350), (820, 470), (950, 470), (1100, 470), (820, 600), (950, 600), (1100, 600)]

def get_pixel_color(x, y):
    return pyautogui.pixel(x, y)

def click(x, y):
    pyautogui.click(x=x, y=y)

white_pixels = []


def main():
    current_round = 1
    while True:
        for x, y in pixel_locations:
            current_color = get_pixel_color(x, y)
            if current_color == (255, 255, 255):
                if white_pixels and white_pixels[-1] == (x, y):
                    continue
                else:
                    white_pixels.append((x, y))


                    

        print(white_pixels)
        print(f'Round: {current_round}')

        if len(white_pixels) == current_round:
            for x, y in white_pixels:
                if white_pixels:
                    time.sleep(0.5)
                    click(x, y)
            white_pixels.clear()
            current_round += 1
            
        

try:
    main()
except Exception as e:
    print(str(e))
    time.sleep(10000)