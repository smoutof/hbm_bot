from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pyautogui, time


# Set up Firefox options
options = Options()
options.headless = False  # Set to True if you don't want a visible browser window

# Specify the Firefox path
firefox_binary_path = "C:\\Users\\orasa\\AppData\\Local\Mozilla Firefox\\firefox.exe"  # Replace with your Firefox path

# Specify the path to the GeckoDriver executable
geckodriver_path = "./geckodriver.exe"

 # Create a Firefox WebDriver instance with the specified paths
driver = webdriver.Firefox(options=options, executable_path=geckodriver_path, firefox_binary=firefox_binary_path)


# Open Human Benchmark typing test in Firefox
url = "https://humanbenchmark.com/tests/typing"
driver.get(url)

# Wait for some time for page to load
driver.implicitly_wait(50)

# Get the HTML from page
html_source = driver.page_source

# Parse the HTML
soup = BeautifulSoup(html_source, 'html.parser')

# Extract text from the text box
text_div = soup.find('div', class_='letters notranslate')

# Make a string
final_text = ""

# Add the letters from the text_div to string
for span in text_div:
    final_text += span.text

# Wait some time before writing
time.sleep(8)

# Write the text
pyautogui.typewrite(final_text)