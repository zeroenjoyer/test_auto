from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.webdriver.support.ui import Select
import os


def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(
        5
    )  # говорим WebDriver искать каждый элемент в течение 5 секунд (на каждый find_element)
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".btn").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # alert = browser.switch_to.alert
    # alert.accept()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(int(x))

    browser.find_element(By.ID, "answer").send_keys(y)

    # checkbox = browser.find_element(By.ID, 'robotCheckbox')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)

    # select = Select(browser.find_element(By.ID, "dropdown"))
    # select.select_by_value(z1)

    # current_dir = os.path.abspath(os.path.dirname(__file__))
    # file_name = "file.txt"
    # file_path = os.path.join(current_dir, file_name)
    # element = browser.find_element(By.ID, "file")
    # element.send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, ".btn").click()

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

    print(browser.switch_to.alert.text.split(": ")[-1])

finally:
    time.sleep(10)
    browser.quit()
