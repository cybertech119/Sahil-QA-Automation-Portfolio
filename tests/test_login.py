# tests/test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def test_login_demo():
    # Using a known demo site for login
    url = "https://the-internet.herokuapp.com/login"
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url)
        time.sleep(1)

        # locate username/password and login button
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(1)

        # assert login success (check for flash message)
        flash = driver.find_element(By.ID, "flash").text
        assert "You logged into a secure area!" in flash

    finally:
        driver.quit()
