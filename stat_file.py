#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""

# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth

from qiniu import BucketManager

from qiniu_api_wrapper import get_ak_sk


access_key, secret_key = get_ak_sk()

#初始化Auth状态
q = Auth(access_key, secret_key)
#初始化BucketManager
bktMgr = BucketManager(q)
#你要测试的空间， 并且这个key在你空间中存在
bucket_name = 'face-data'
key = 'python-logo.png'
#获取文件的状态信息
ret, info = bktMgr.stat(bucket_name, key)
print(info)
assert 'hash' in ret