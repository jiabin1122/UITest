# -*- coding: utf-8 -*-
# @Author: Jiabin

import os
import json


def save_cookies(cookies):
    path = os.path.join(os.getcwd(),"data","cookies.txt")
    cookie = {}
    for item in cookies:
        cookie[item['name']] = item['value']
    with open(path,"wb") as f:
        f.write(json.dumps(cookie))

def get_cookies():
    with open("./data/cookies.txt", "r") as f:
        cookies = eval(f.read())
    return cookies

