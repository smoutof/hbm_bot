from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pyautogui, time


try:
    # Set up Firefox options
    options = Options()
    options.headless = False  # Set to True if you don't want a visible browser window

    # Specify the path to the Firefox binary
    firefox_binary_path = "C:\\Users\\orasa\\AppData\\Local\Mozilla Firefox\\firefox.exe"  # Replace with your firefox path

    # Specify the path to the GeckoDriver executable
    geckodriver_path = "./geckodriver.exe"

    # Create a Firefox WebDriver instance with the specified paths
    driver = webdriver.Firefox(options=options, executable_path=geckodriver_path, firefox_binary=firefox_binary_path)


    # Open a website in Firefox
    url = "https://humanbenchmark.com/tests/typing"
    driver.get(url)

    # Wait for some time to ensure the page loads
    driver.implicitly_wait(50)

    # Get the HTML source of the page
    html_source = driver.page_source

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html_source, 'html.parser')

    # Extract text from human benchmark text box
    text_div = soup.find('div', class_='letters notranslate')

    # Make the final string
    final_text = ""

    # Add the letters from the text_div to 
    for span in text_div:
        final_text += span.text

    print(final_text)
    time.sleep(8)
    pyautogui.typewrite(final_text)
except Exception as e:
    print(f'Error: {str(e)}')
    input()
