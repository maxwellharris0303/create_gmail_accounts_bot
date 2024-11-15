from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Set the path to your Chrome driver executable

# Set the path to the directory where you want to create the profile
profile_directory = 'C:/Users/root/AppData/Local/Google/Chrome/User Data/Profile 1001'

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=' + profile_directory)

# Create a new Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open any website to initialize the profile
driver.get('https://www.example.com')

driver.start_client
# sleep(100)
# At this point, the new profile has been created and initialized.
# You can customize the profile further or use it for your specific needs.
driver.quit()

# import shutil

# # Set the path to the directory of the profile you want to delete
# profile_directory = 'C:/Users/root/AppData/Local/Google/Chrome/User Data/Profile 1234'

# # Delete the profile directory
# shutil.rmtree(profile_directory)

# print("Chrome profile deleted successfully.")