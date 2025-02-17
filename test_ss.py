import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://google.com"

def test_one():
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.ID, 'gb')

    time.sleep(7)

if __name__ == "__main__":
    pytest.main()