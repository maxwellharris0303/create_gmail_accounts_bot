from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# Selenium Wire configuration to use a proxy
# PROXY_USERNAME = "t3vUnZxqkoTi6s6j"
# PROXY_PASSWORD = "PKqAWxzwyHPuMp3v_streaming-1"
# seleniumwire_options = {
#     'proxy': {
#         'http': f'http://{PROXY_USERNAME}:{PROXY_PASSWORD}@geo.iproyal.com:12321',
#         'verify_ssl': False,
#     },
# }

# driver = webdriver.Chrome(
#     seleniumwire_options=seleniumwire_options
# )
PROXY_USERNAME = "root"
PROXY_PASSWORD = "future123"

seleniumwire_options = {
    'proxy': {
        'http': f'http://{PROXY_USERNAME}:{PROXY_PASSWORD}@35.94.102.9:3128',
        'verify_ssl': False,
    },
}

driver = webdriver.Chrome(
    seleniumwire_options=seleniumwire_options
)


driver.get('http://httpbin.org/ip')


sleep(1000)