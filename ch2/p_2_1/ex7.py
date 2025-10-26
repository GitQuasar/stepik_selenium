import time
from math import log, sin

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.binary_location = "/usr/bin/chromium-browser"
browser = webdriver.Chrome(options=options)

try:
    browser.get("http://suninjuly.github.io/get_attribute.html")
    x = browser.find_element(By.ID, "treasure")
    x_value = int(x.get_attribute("valuex"))
    browser.find_element(By.ID, "answer").send_keys(str(log(abs(12 * sin(x_value)))))
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
except Exception as e:
    print(f"Error: {e}")
finally:
    time.sleep(5)
    browser.quit()  # Always quit the browser, even if an error occurs
