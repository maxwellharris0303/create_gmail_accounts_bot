from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import keyboard

EMAIL_ADDRESS = "Albahirefeedbird@gmail.com"
PASSWORD = "Siraj@333"
options = webdriver.ChromeOptions() 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.maximize_window()
# driver.get('http://httpbin.org/ip')

driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Faccounts.google.com%2F&followup=https%3A%2F%2Faccounts.google.com%2F&ifkv=ASKXGp24us3FXc2oQRQkfXm92n5_tWihF1_8ztD1wl1lcc8hSq0A0scZ_LmrH77qXEsvkkWTGhpp&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1761682904%3A1702569847247040&theme=glif")

# sleep(1000)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))

email_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
email_input.send_keys(EMAIL_ADDRESS)

next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next_button.click()


sleep(1000)
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