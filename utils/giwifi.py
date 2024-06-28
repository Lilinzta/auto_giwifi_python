from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from .crypto_encode import crypto_encode
from selenium import webdriver
from bs4 import BeautifulSoup
import requests


class giwifi:

    def __init__(self, base_url, login_url):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.wait = WebDriverWait(self.driver, 3)
        self.base_url = base_url
        self.login_url = login_url

    def login(self, username, password):
        self.driver.get(self.login_url)

        first_name = self.wait.until(
            EC.presence_of_element_located((By.ID, 'first_name')))
        first_password = self.wait.until(
            EC.presence_of_element_located((By.ID, 'first_password')))
        login_btn = self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'form-input.submit_btn')))

        first_name.send_keys(username)
        first_password.send_keys(password)
        login_btn.click()
        print('login successfully!')

    def close(self):
        self.driver.quit()

    def logout(self, headers, user_info):
        url = f"{self.base_url}/gportal/web/login"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            iv = soup.find(id="iv")['value']

            form = soup.find('form', {'id': 'frmLogin'})
            form_data = {tag['name']: tag['value']
                         for tag in form.find_all('input') if tag.has_attr('name')}

            form_data['name'] = user_info['username']
            form_data['password'] = user_info['password']

            ori_data = '&'.join(f"{key}={value}" for key,
                                value in form_data.items())
            msg = crypto_encode(ori_data, iv)

            data_obj = {
                "ivv": iv,
                "msg": msg,
            }

            url = f"{self.base_url}/gportal/web/authLogout"
            data = {
                'data': data_obj['msg'],
                'iv': data_obj['ivv']
            }

            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 200:
                print("logout successfully!")
        else:
            print("Error fetching the webpage:", response.status_code)
