from utils.giwifi import giwifi
import time
import toml

with open('config.toml', 'r') as file:
    config = toml.load(file)

uname = config['user_info']['uname']
passwd = config['user_info']['passwd']

user_info = {
    'username': uname,
    'password': passwd,
}

base_url = config['base_url']
login_url = config['login_url']

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

if __name__ == "__main__":

    giwifi = giwifi(base_url, login_url)
    while True:
        giwifi.logout(headers, user_info)
        giwifi.login(uname, passwd)
        print("sleep 9m55s for next login")
        time.sleep(595)
    giwifi.close()
