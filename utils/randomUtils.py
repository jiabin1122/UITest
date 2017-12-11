# -*- coding: utf-8 -*-
# @Author: Jiabin

import string
import random


def generate_random_string(count=10):
    random_string = ''.join(random.sample(string.letters.lower() + string.digits,count))
    return random_string

def generate_random_int(min, max):
    return random.randint(min, max)

