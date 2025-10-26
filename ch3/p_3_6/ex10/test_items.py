import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_item_add_to_basket(browser: webdriver.Chrome):
    browser.get(link)
    time.sleep(5)
    basket = browser.find_element(By.CSS_SELECTOR, "form button.btn-add-to-basket")
    assert basket.text, "Element not found"
    print(basket.text)
