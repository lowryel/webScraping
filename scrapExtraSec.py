import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import codecs

import re

from webdriver_manager.firefox import GeckoDriverManager


# chromeOptions = uc.ChromeOptions()
# chromeOptions.headless = True
# driver = uc.Chrome(options=chromeOptions)
# firefox_binary_path = "/usr/bin/firefox"
# driver_options = webdriver.FirefoxOptions()
# driver_options.binary_location = firefox_binary_path

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=webdriver.FirefoxOptions)

driver.get("https://www.upwork.com/ab/account-security/login")
# time.sleep(10)

loginOption = driver.find_element(By.ID, "login_google_submit").click()
main_window= driver.current_window_handle
all_window_handle= driver.window_handles
for handle in all_window_handle:
    if handle != main_window:
        driver.switch_to.window(handle)
        break

# # Perform actions on the popup window
# # For example, you can find elements and interact with them
# popup_element = driver.find_element(By.CLASS_NAME, "LbOduc")
# popup_element.click()
# time.sleep(5)
# # popup_element.send_keys("Hello, popup!")

# nickname = driver.find_element(By.ID, "login_answer")
# nickname.send_keys("Your best friend Nickname")

# driver.find_element(By.ID, "login_control_continue").click()
# driver.quit()
