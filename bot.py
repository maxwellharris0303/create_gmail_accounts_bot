from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep
import requests
import keyboard

PROXY_USERNAME = "t3vUnZxqkoTi6s6j"
PROXY_PASSWORD = "PKqAWxzwyHPuMp3v_streaming-1"

proxy_server = 'http://geo.iproyal.com:12321'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={proxy_server}')

FIRST_NAME = "Oscar"
PASSWORD = "12SFDF34qwesdfr!@#$"

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://accounts.google.com/signup/v2/createaccount?biz=false&cc=RU&continue=https%3A%2F%2Faccounts.google.com%2F&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=AVQVeyykUFunHz9c4MPy3MHKrgizQg5OX87DTeSHi16xdtLUSXNHQKKthoKrYy23LbN1P0nmZZ1h9g&theme=glif")

sleep(2)
keyboard.write(PROXY_USERNAME)
keyboard.press('tab')
keyboard.release('tab')
keyboard.write(PROXY_PASSWORD)
keyboard.press('tab')
keyboard.release('tab')
keyboard.press('enter')
keyboard.release('enter')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"text\"]")))

sleep(1000)

first_name_input = driver.find_elements(By.CSS_SELECTOR, "input[type=\"text\"]")[0]
first_name_input.send_keys(FIRST_NAME)

next_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"button\"]")
next_button.click()

day_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"day\"]")))
day_element.send_keys("8")

month_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[aria-labelledby=\"month-label\"]")))
month_element.click()

sleep(1)

option_month = month_element.find_element(By.CSS_SELECTOR, "option[value=\"4\"]")
print(option_month)
option_month.click()

year_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id=\"year\"]")))
year_element.send_keys("1996")

gender_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[aria-labelledby=\"gender-label\"]")))
gender_element.click()
sleep(1)
option_gender = gender_element.find_element(By.CSS_SELECTOR, "option[value=\"3\"]")
option_gender.click()

next_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"button\"]")
next_button.click()

try:
    gmail_input = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"text\"]")))
    gmail_input.send_keys(FIRST_NAME + "345")
    next_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"button\"]")
    next_button.click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=\"fBRZbb TrZEUc\"]")))
    suggested_gmails = driver.find_elements(By.CSS_SELECTOR, "button[class=\"fBRZbb TrZEUc\"]")
    suggested_gmails[0].click()
except:
    driver.find_elements(By.CSS_SELECTOR, "div[class=\"SCWude\"]")[0].click()



next_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"button\"]")
next_button.click()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))

password_elements = driver.find_elements(By.CSS_SELECTOR, "input[type=\"password\"]")
password_elements[0].send_keys(PASSWORD)
password_elements[1].send_keys(PASSWORD)

next_button = driver.find_element(By.CSS_SELECTOR, "button[type=\"button\"]")
next_button.click()

sleep(1000)