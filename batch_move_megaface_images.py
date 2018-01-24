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
access_key, secret_key = get_ak_sk('./ak_sk_avatest.json')

##################################################
# configs
bucket = 'identities-dataset'
bucket2 = 'face-megaface-images'
#prefix = 'Celeb'
prefix = 'assets/megaface/identities_all/'

prefix_len = len(prefix)

max_list_cnt = None

contains_str = None
#contains_str = ['.zip', '.tgz', '.tar.gz', '.whl', 'sh']
# contains_str = ['.mat']
contains_str2 = ['']
# contains_str2 = ['lfw']
##################################################333

##################################################333
# generate key in bucket2
# def get_new_key(key):
#     return key


def get_new_key(key):
    new_key = key[prefix_len:]
    return new_key
##################################################333


# 初始化Auth状态
q = Auth(access_key, secret_key)
# 初始化BucketManager
bktMgr = BucketManager(q)
# 你要测试的空间， 并且这个key在你空间中存在


marker = None
while True:
    # 获取文件的状态信息
    ret = bktMgr.list(bucket, prefix, marker, max_list_cnt)

    if not ret[0]:
        print "No qualified files in the bucket"
        break

    items = ret[0]['items']

    if contains_str:
        #        key_list = [it['key']
        #                    for it in items if contains_str in it['key'].lower()]
        #        if save_details:
        #            key_list_detail = [
        # it for it in items if contains_str in it['key'].lower()]
        key_list = []
        key_list_detail = []
        for i in range(len(items)):
            for sub_str in contains_str:
                if sub_str in items[i]['key'].lower():
                    key_list.append(items[i]['key'])
                    break
    else:
        key_list = [it['key'] for it in items]

    if contains_str2:
        key_list_2 = []
        key_list_detail_2 = []
        for i in range(len(key_list)):
            for sub_str in contains_str2:
                if sub_str in key_list[i].lower():
                    key_list_2.append(key_list[i])
                    break

        key_list = key_list_2

    # print key_list
    fetch_cnt = len(key_list)
    print "%d qualified files found" % fetch_cnt

    first_n = min(fetch_cnt, 10)
    print "---> First %d files:" % first_n
    for i in range(first_n):
        print '%d --> %s' % (i + 1, key_list[i])

    #json.dump(key_list, fp, indent=2)

    for key in key_list:
        key2 = get_new_key(key)
        ret2 = bktMgr.move(bucket, key, bucket2, key2)
        print '\n==========bucket.move() returns:'
        if ret2:
            print ret2
        else:
            print 'Succeeded to move'

    if 'marker' in ret[0]:
        print 'Returned marker is: ', marker
        print 'More files to list'
        marker = ret[0]['marker']

        if max_list_cnt:
            max_list_cnt = max_list_cnt - fetch_cnt
    else:
        print 'No more files, list fininshed'
        break
