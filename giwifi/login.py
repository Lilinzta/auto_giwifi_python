from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(username, password, open_url):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)

    driver.get(open_url)
    wait = WebDriverWait(driver, 10)
    first_name = wait.until(
        EC.presence_of_element_located((By.ID, 'first_name')))
    first_password = wait.until(
        EC.presence_of_element_located((By.ID, 'first_password')))
    login_btn = wait.until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'form-input.submit_btn')))

    first_name.send_keys(username)
    first_password.send_keys(password)
    login_btn.click()
    driver.get_screenshot_as_file("login.png")

    print("relogin successfully!")

    driver.quit()
