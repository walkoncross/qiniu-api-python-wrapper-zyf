#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""

from qiniu import Auth

from qiniu import BucketManager

from ak_sk import get_ak_sk

# get ak,sk
access_key, secret_key = get_ak_sk()

##################################################
# configs
bucket = 'face-recog-sphereface-webface'
bucket2 = bucket
#prefix = 'lfw'
prefix = 'sphereface-64-prototxt/sphereface_64_train_bs256_1007'

contains_str = None
#contains_str = 'celeb'

##################################################333

##################################################333
# generate key in bucket2
# def get_new_key(key):
#     return key


def get_new_key(key):
    new_key = key.replace('sphereface-64-prototxt', 'train-results')
    return new_key
##################################################333


#初始化Auth状态
q = Auth(access_key, secret_key)
#初始化BucketManager
bktMgr = BucketManager(q)
#你要测试的空间， 并且这个key在你空间中存在

#获取文件的状态信息
ret = bktMgr.list(bucket, prefix)

items = ret[0]['items']

if contains_str:
    key_list = [it['key'] for it in items if contains_str in it['key'].lower()]
else:
    key_list = [it['key'] for it in items]
print key_list

for key in key_list:
    key2 = get_new_key(key)
    ret2 = bktMgr.move(bucket, key, bucket2, key2)
    print '\n==========bucket.move() returns:'
    if ret2:
        print ret2
    else:
        print 'Succeeded to move'