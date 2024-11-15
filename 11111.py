from selenium_driverless.sync import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

EMAIL_ADDRESS = "Alfietryffeedbirrdz@gmail.com"
PASSWORD = "Siraj@333"

RECOVERY_EMAIL_ADDRESS = "Stefan.weydt@gmail.com"
CAMPAIGN_NAME = "Edvin"

profile_directory = 'C:/Users/root/AppData/Local/Google/Chrome/User Data/Profile 1001'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=' + profile_directory)
driver = webdriver.Chrome(options=chrome_options)

driver.get('http://accounts.google.com')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))
email_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
email_input.write(EMAIL_ADDRESS)

next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
next_button.click()

sleep(3)

password_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"password\"]")
password_input.write(PASSWORD)

next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
next_button.click()
sleep(5)
# cookies = driver.get_cookies()
# print(cookies)
driver.get("http://accounts.google.com")
sleep(5)
driver.quit()