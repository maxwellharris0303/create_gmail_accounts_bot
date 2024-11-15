from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:/Users/root/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument('--profile-directory=Profile 1')  # Replace with the actual Chrome profile directory
# chrome_options.add_argument('--disable-dev-shm-usage')

chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# chrome_driver.maximize_window()

# chrome_driver.get("https://temp-mail.org")

sleep(1000)