from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import keyboard

PROXY_USERNAME = "t3vUnZxqkoTi6s6j"
PROXY_PASSWORD = "PKqAWxzwyHPuMp3v_streaming-1"

proxy_server = 'http://geo.iproyal.com:12321'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy_server}')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://icanhazip.com/")

sleep(2)
keyboard.write(PROXY_USERNAME)
keyboard.press('tab')
keyboard.release('tab')
keyboard.write(PROXY_PASSWORD)
keyboard.press('tab')
keyboard.release('tab')
keyboard.press('enter')
keyboard.release('enter')

sleep(1000)