from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

# Create Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
hearders = [{
'authority': 'accounts.google.com',
'accept': '*/*',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
'cookie': 'CONSENT=PENDING+108; SOCS=CAISHAgCEhJnd3NfMjAyMzEyMDUtMF9SQzIaAmZpIAEaBgiAucmrBg; AEC=Ackid1RKqCvO1nNAybUHrUDZGdm5CftRCRQJyHeucTmISqKcfS7BqqZ2fQ; NID=511=BdD3-1OlkxU5ZhPTzqzGV6D9p0nVqtG-sbedT3cjeBmM9pkQ0ZP1pNUlbqlxVsuNz8IgRzQjg8jCq4wYW847NSSXlDO7bBNBdSfpADhk61vIhvbT51-IGFY3YN0GNeyMySUXP7h9WgXiq9XDAEbnTOsV9ERGLot91COzc9HJ4CDuyTF5TUWIZuZXudUIcK41AbkTB5dwYNfb; __Host-GAPS=1:-CalUx0kScNErpFHpi50VfopM2K97w:IjAlapM4gq97fP7o; OTZ=7339070_48_48_123900_44_436380',
'origin': 'https://accounts.google.com',
'referer': 'https://accounts.google.com/',
'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
'sec-ch-ua-arch': '"x86"',
'sec-ch-ua-bitness': '"64"',
'sec-ch-ua-full-version': '"120.0.6099.71"',
'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.71", "Google Chrome";v="120.0.6099.71"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-model': '""',
'sec-ch-ua-platform': '"Windows"',
'sec-ch-ua-platform-version': '"10.0.0"',
'sec-ch-ua-wow64': '?0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=5c6c9e62-a124-491f-b099-f9631e75fdd1,signin_mode=all_accounts,signout_mode=show_confirmation',
'x-client-data': 'CI+2yQEIpbbJAQipncoBCPeKywEIlKHLAQib/swBCIWgzQEI9qbNAQjcvc0BCI7hzQEI2+nNAQji7M0BCKfuzQEIg/DNARjG4c0BGKfqzQE=',
'x-same-domain': '1'
}]
# Set the User-Agent header
chrome_options.add_argument(f"user-agent={hearders[0]}")

# Create the webdriver instance with the options
driver = webdriver.Chrome(options=chrome_options)

# Your code here...

# Quit the webdriver

# driver.get("https://httpbin.org/headers")
driver.get("https://accounts.google.com")

EMAIL_ADDRESS = "Antontryffeedbirds@gmail.com"
PASSWORD = "Siraj@333"

email_input = driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]")
email_input.send_keys(EMAIL_ADDRESS)

next_button = driver.find_elements(By.TAG_NAME, 'button')
print(len(next_button))
next_button[0].click()

driver.save_screenshot("screenshot.png")

sleep(1000)
hearders = [{
'authority': 'accounts.google.com',
'accept': '*/*',
'accept-language': 'en-US,en;q=0.9',
'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
'cookie': 'CONSENT=PENDING+108; SOCS=CAISHAgCEhJnd3NfMjAyMzEyMDUtMF9SQzIaAmZpIAEaBgiAucmrBg; AEC=Ackid1RKqCvO1nNAybUHrUDZGdm5CftRCRQJyHeucTmISqKcfS7BqqZ2fQ; NID=511=BdD3-1OlkxU5ZhPTzqzGV6D9p0nVqtG-sbedT3cjeBmM9pkQ0ZP1pNUlbqlxVsuNz8IgRzQjg8jCq4wYW847NSSXlDO7bBNBdSfpADhk61vIhvbT51-IGFY3YN0GNeyMySUXP7h9WgXiq9XDAEbnTOsV9ERGLot91COzc9HJ4CDuyTF5TUWIZuZXudUIcK41AbkTB5dwYNfb; __Host-GAPS=1:-CalUx0kScNErpFHpi50VfopM2K97w:IjAlapM4gq97fP7o; OTZ=7339070_48_48_123900_44_436380',
'origin': 'https://accounts.google.com',
'referer': 'https://accounts.google.com/',
'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
'sec-ch-ua-arch': '"x86"',
'sec-ch-ua-bitness': '"64"',
'sec-ch-ua-full-version': '"120.0.6099.71"',
'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.71", "Google Chrome";v="120.0.6099.71"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-model': '""',
'sec-ch-ua-platform': '"Windows"',
'sec-ch-ua-platform-version': '"10.0.0"',
'sec-ch-ua-wow64': '?0',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=5c6c9e62-a124-491f-b099-f9631e75fdd1,signin_mode=all_accounts,signout_mode=show_confirmation',
'x-client-data': 'CI+2yQEIpbbJAQipncoBCPeKywEIlKHLAQib/swBCIWgzQEI9qbNAQjcvc0BCI7hzQEI2+nNAQji7M0BCKfuzQEIg/DNARjG4c0BGKfqzQE=',
'x-same-domain': '1'
}]