from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
EMAIL_ADDRESS = "Antontryffeedbirds@gmail.com"
PASSWORD = "Siraj@333"
# Configure Chrome options
chrome_options = webdriver.FirefoxOptions()
chrome_options.add_argument("--headless")

# Create a new instance of the Chrome driver
driver = webdriver.Firefox(options=chrome_options)

# Use the driver to interact with the browser
driver.get("https://accounts.google.com")
# Perform other actions like clicking elements, filling forms, etc.

email_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
email_input.send_keys(EMAIL_ADDRESS)

next_button = driver.find_elements(By.TAG_NAME, 'button')
print(len(next_button))
next_button[0].click()

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"password\"]")))
sleep(3)

password_input = driver.find_element(By.TAG_NAME, "input")
print(password_input.get_attribute('type'))
password_input.send_keys(PASSWORD)

next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
next_button.click()

driver.save_screenshot("screenshot.png")
