from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

firefox_profile_directory = 'C:/Users/root/AppData/Roaming/Mozilla/Firefox/Profiles/tzz8lrje.default'
firefox_options = webdriver.FirefoxOptions()
firefox_options.profile = webdriver.FirefoxProfile(firefox_profile_directory)

driver = webdriver.Firefox(options=firefox_options)

driver.get("https://myaccount.google.com/profile")