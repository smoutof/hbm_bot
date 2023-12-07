from pathlib import Path
import pyautogui

#######################
# pyautogui functions #
#######################

# Pixel color function using pyautogui
def get_pixel_color(x, y):
    return pyautogui.pixel(x, y)

# Click function using pyautogui
def click(x, y):
    pyautogui.click(x=x, y=y)


#############################
# firefox finding functions #
#############################

# Get the users home path
home = Path.home()

# Paths
firefox = "firefox.exe" 
default_64_bit = "C:/Program Files/Mozilla Firefox/"
default_32_bit = "C:/Program Files (x86)/Mozilla Firefox/"
appdata_local = f'{home}/Appdata/Local/Mozilla Firefox/'

paths = [default_64_bit, default_32_bit, appdata_local] # All paths in list

# Check if the file exists
def file_exists(directory, file_name):
    file_path = Path(directory) / file_name
    return file_path.is_file() # Returns True or False

# Main function
def findFirefox():
    firefox_exists = False
    confirmed_path = ""

    # Check path list
    for path in paths:
        if file_exists(path, firefox):
            print(f'{firefox} found in {path}!')
            firefox_exists = True
            confirmed_path = f'{path}{firefox}'
        else:
            print(f'{firefox} not found in {path}!')
    
    # If Firefox wasn't found anywhere.
    if not firefox_exists:
        print("Firefox not found!")
        print("It seems like Firefox isn't installed, or it's installed in a custom location.")
        return False
    else:
        return confirmed_path