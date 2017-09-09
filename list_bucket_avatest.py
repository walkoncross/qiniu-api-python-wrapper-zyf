#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""

from qiniu import Auth
from qiniu import BucketManager

import json

from ak_sk import get_ak_sk


#access_key, secret_key = get_ak_sk()
access_key, secret_key = get_ak_sk('ak_sk_avatest.json')

save_details = False

bucket_name = 'identities-dataset'
#prefix = 'lfw'
#prefix = None
prefix = 'assets/face_card_data'
max_list_cnt = 2000 # set to None for no limit
contains_str = 'jpg'

rlt_list_file = bucket_name + '_key_list.json'
fp = open(rlt_list_file, 'w')

if save_details:
    rlt_list_file2 = bucket_name + '_key_list_details.json'
    fp2 = open(rlt_list_file2, 'w')
    fp2.write('[\n')

#初始化Auth状态
q = Auth(access_key, secret_key)
#初始化BucketManager
bktMgr = BucketManager(q)
#你要测试的空间， 并且这个key在你空间中存在

marker = None
while True:
    #获取文件的状态信息
    ret = bktMgr.list(bucket_name, prefix, marker, max_list_cnt)

    if not ret[0]:
        print "No qualified files in the bucket"
        break

    items = ret[0]['items']

    if contains_str:
        key_list = [it['key'] for it in items if contains_str in it['key'].lower()]
        if save_details:
            key_list2 = [it for it in items if contains_str in it['key'].lower()]
    else:
        key_list = [it['key'] for it in items]
        if save_details:
            key_list2 = [it for it in items]

    #print key_list
    fetch_cnt = len(key_list)
    print "%d qualified files found" % fetch_cnt

    #json.dump(key_list, fp, indent=2)

    for it in key_list:
        fp.write(it+'\n')

    if save_details:
#        json.dump(key_list2, fp2, indent=2)
        for it in key_list2:
            json.dump(it, fp2, indent=2)
            fp2.write(',\n')

    if 'marker' in ret[0]:
        print 'Returned marker is: ', marker
        print 'More files to list'
        marker = ret[0]['marker']

        if max_list_cnt:
            max_list_cnt = max_list_cnt - fetch_cnt
    else:
        print 'No more files, list fininshed'
        break

fp.close()

if save_details:
    fp2.write('"end of list, skip this item"]\n')
    fp2.close()