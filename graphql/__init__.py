import requests
import re
from typing import Union
from . import action, config, tools, utils

class Facebook:
    def __init__(self, cookie: Union[str, dict]) -> None:
        self.session = requests.session()

        if isinstance(cookie, str): 
            self.session.cookies['cookie'] = cookie
            self.uid = re.search(r'c_user=(.*?)\&', cookie).group(1)
            self.cookie = cookie
        elif isinstance(cookie, dict): 
            self.session.cookies.update(cookie)
            self.uid = cookie['c_user']
            self.cookie = '; '.join(f'{k}={v}' for k, v in cookie.items())

    def __str__(self) -> str:
        return f'Facebook: [id: {self.uid}] Cookie: {self.cookie}'

    def __repr__(self) -> str:
        return f'Facebook: [id: {self.uid}] Cookie: {self.cookie}'

print(Facebook(cookie='c_user=19293939&'))

