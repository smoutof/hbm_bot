import pyautogui
import time
from Resources import funcs

# Define pixel locations of Human Benchmark sequence memory tile locations
pixel_locations = [(820, 350), (950, 350), (1100, 350), (820, 470), (950, 470), (1100, 470), (820, 600), (950, 600), (1100, 600)] # Change for your dimensions. (Using 1920x1080, with scaling at 100% on Windows)


# Make a list for pixels that are white
white_pixels = []

# Main loop function
def main():
    current_round = 1 # Round variable, changes with the sequence memory levels
    while True:
        for x, y in pixel_locations: # Check the pixels
            current_color = funcs.get_pixel_color(x, y) # Get the color
            if current_color == (255, 255, 255): # If color is white
                if white_pixels and white_pixels[-1] == (x, y): # If white pixels list has pixel locations and the last pixel location isn't the same as the current pixel location
                    continue
                else:
                    white_pixels.append((x, y)) # Else add the current pixel location to the list


                    

        print(f'Length of white pixels list: {len(white_pixels)}') # Prints the number of items in white pixels
        print(f'Round: {current_round}') # Prints the round

        if len(white_pixels) == current_round: # If the length of list is the same as the current round
            for x, y in white_pixels: # For every pixel location
                if white_pixels: # If list isn't empty
                    time.sleep(0.5)
                    funcs.click(x, y) # Click at the location

            # Clear the list and increment the round after done
            white_pixels.clear()
            current_round += 1
            
        


main()