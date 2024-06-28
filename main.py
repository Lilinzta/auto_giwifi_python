from giwifi.logout import logout
from giwifi.login import login
import logging
import time
import toml

logging.disable(logging.CRITICAL)

with open('config.toml', 'r') as file:
    config = toml.load(file)

uname = config['user_info']['uname']
passwd = config['user_info']['passwd']

user_info = {
    'username': uname,
    'password': passwd,
}

base_url = config['base_url']
open_url = config['open_url']

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

if __name__ == "__main__":
    while True:
        logout(base_url, headers, user_info)
        login(uname, passwd, open_url)
        print("sleep 9m30s for next login")
        time.sleep(570)
