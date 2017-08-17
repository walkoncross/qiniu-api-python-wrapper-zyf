# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""

from qiniu import Auth
from qiniu import BucketManager

import json

from ak_sk import get_ak_sk


access_key, secret_key = get_ak_sk()

bucket_name = 'face-data'
#prefix = 'lfw'
prefix = None

contains_str = 'zip'

rlt_list_file = bucket_name + '_key_list.json'
rlt_list_file2 = bucket_name + '_key_list_details.json'

fp = open(rlt_list_file, 'w')
fp2 = open(rlt_list_file2, 'w')

#初始化Auth状态
q = Auth(access_key, secret_key)
#初始化BucketManager
bucket = BucketManager(q)
#你要测试的空间， 并且这个key在你空间中存在

#获取文件的状态信息
ret = bucket.list(bucket_name, prefix)

items = ret[0]['items']

if contains_str:
    key_list = [it['key'] for it in items if contains_str in it['key'].lower()]
    key_list2 = [it for it in items if contains_str in it['key'].lower()]
else:
    key_list = [it['key'] for it in items]
    key_list2 = [it for it in items]

print key_list

json.dump(key_list, fp, indent=4)
fp.close()

json.dump(key_list2, fp2, indent=4)
fp2.close()
