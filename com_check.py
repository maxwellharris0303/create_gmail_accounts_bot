from selenium import webdriver
from time import sleep

PROXY_USERNAME = "t3vUnZxqkoTi6s6j"
PROXY_PASSWORD = "PKqAWxzwyHPuMp3v_streaming-1"
proxy_server = 'http://geo.iproyal.com:12321'

user_agent_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36"

# Set Chrome options to retrieve the user agent string
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without opening a browser window)
chrome_options.add_argument(f"user-agent={user_agent_string}")
chrome_options.add_argument(f'--proxy-server={proxy_server}')

# Instantiate the Chrome webdriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Get the user agent string
user_agent = driver.execute_script("return navigator.userAgent;")

# Print the user agent string
print(user_agent)

# Close the browser

sleep(3000)

driver.quit()