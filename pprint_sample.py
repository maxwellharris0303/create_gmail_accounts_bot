from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def login_google_account(emails: list[str], password: str) -> bool:
    """
    Logs into a Google account using Selenium.

    This function attempts to log into a Google account using a list of email addresses
    and a password. It iterates through the email addresses until a successful login
    is achieved or all email addresses have been tried.

    Parameters:
    - emails (list[str]): A list of email addresses to try for login.
    - password (str): The password for the Google account.

    Returns:
    bool: True if the login is successful, False otherwise.

    Raises:
    - ValueError: If the list of email addresses is empty or if the password is empty.
    """

    # Validating the inputs
    if not emails:
        raise ValueError("Email list cannot be empty.")
    if not password:
        raise ValueError("Password cannot be empty.")
    options = webdriver.ChromeOptions() 

    # Setting up the Selenium WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        # Iterating through the email addresses
        for email in emails:
            # Opening the Google login page
            driver.get("https://accounts.google.com")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"email\"]")))

            # Finding the email input field and entering the email address
            email_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
            email_input.send_keys(email)
            email_input.send_keys(Keys.RETURN)

            # Finding the password input field and entering the password
            password_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"password\"]")
            sleep(1000)
            password_input.send_keys(password)
            password_input.send_keys(Keys.RETURN)

            # Checking if the login was successful
            if "myaccount.google.com" in driver.current_url:
                # Successful login
                return True

        # All email addresses have been tried without success
        return False

    finally:
        # Closing the browser window
        driver.quit()

# Example usage:

# List of email addresses to try for login
emails = ["example1@gmail.com", "example2@gmail.com", "example3@gmail.com"]

# Password for the Google account
password = "password123"

# Attempting to login
login_successful = login_google_account(emails, password)

# Printing the result
if login_successful:
    print("Login successful!")
else:
    print("Login failed.")