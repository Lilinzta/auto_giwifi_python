import requests
from bs4 import BeautifulSoup
from .crypto_encode import crypto_encode


def logout(base_url, headers, user_info):
    url = f"{base_url}/gportal/web/login"
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

        url = f"{base_url}/gportal/web/authLogout"
        data = {
            'data': data_obj['msg'],
            'iv': data_obj['ivv']
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            print("logout successfully!")
    else:
        print("Error fetching the webpage:", response.status_code)
