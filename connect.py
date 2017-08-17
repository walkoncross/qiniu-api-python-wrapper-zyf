# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 18:24:09 2017

@author: zhaoy
"""

from qiniu import Auth
from ak_sk import get_ak_sk

access_key, secret_key = get_ak_sk()

q = Auth(access_key, secret_key)