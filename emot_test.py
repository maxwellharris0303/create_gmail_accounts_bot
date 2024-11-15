from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from selenium.webdriver.common.keys import Keys
import asyncio
from time import sleep

EMAIL_ADDRESS = "Albahirefeedbird@gmail.com"
PASSWORD = "Siraj@333"
async def main():
    options = webdriver.ChromeOptions()
    async with webdriver.Chrome(options=options) as driver:
        await driver.get('http://accounts.google.com')
        sleep(2)
        input_email = await driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]", timeout=10)

# async def main():
#     options = webdriver.ChromeOptions()
#     async with webdriver.Chrome(options=options) as driver:
#         await driver.get('http://accounts.google.com')
#         await driver.sleep(0.5)
#         await driver.wait_for_cdp("Page.domContentEventFired", timeout=15)
        
#         # wait 10s for elem to exist
#         input_email = await driver.find_element(By.CSS_SELECTOR, "input[type=\"email\"]", timeout=10)
#         await input_email.write(EMAIL_ADDRESS)
#         await input_email.write(Keys.RETURN)
#         # await elem.click(move_to=True)

#         input_password = await driver.find_element(By.CSS_SELECTOR, "input[type=\"password\"]", timeout=10)
#         await input_password.write(PASSWORD)
#         await input_password.write(Keys.RETURN)


asyncio.run(main())
