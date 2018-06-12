#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 18:24:09 2017

@author: zhaoy
"""

from qiniu import Auth
from qiniu_api_wrapper import get_ak_sk

access_key, secret_key = get_ak_sk()

q = Auth(access_key, secret_key)