# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""

from qiniu import Auth

from qiniu import BucketManager

from ak_sk import get_ak_sk


access_key, secret_key = get_ak_sk()

bucket_name = 'lfw-eval-results'
bucket_name2 = 'face-lfw'
#prefix = 'lfw'
prefix = None

contains_str = None
#contains_str = 'celeb'


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
else:
    key_list = [it['key'] for it in items]
print key_list

for key in key_list:
    ret2 = bucket.move(bucket_name, key, bucket_name2, key)
    print '\n==========bucket.move() returns:'
    if ret2:
        print ret2
    else:
        print 'Succeeded to move'