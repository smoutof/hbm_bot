from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
import pyautogui, time
from Resources import funcs

# Specify the Firefox path
firefox_binary_path = funcs.findFirefox()  # Try to find Firefox path

# If the path wasn't found, do this:
# firefox_binary_path = "C:/Your/Own/Firefox/Path"

if not firefox_binary_path: # If Firefox doesn't exist, quit the program
    input()
    raise SystemExit

# Specify the path to the GeckoDriver executable
geckodriver_path = "./Resources/geckodriver.exe"

# Set up Firefox options
firefox_options = webdriver.FirefoxOptions()
firefox_options.headless = False
firefox_options.binary_location = firefox_binary_path

# Set up service
firefox_service = Service(geckodriver_path)

# Create a Firefox WebDriver instance with the specified paths
driver = webdriver.Firefox(options=firefox_options, service=firefox_service)


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