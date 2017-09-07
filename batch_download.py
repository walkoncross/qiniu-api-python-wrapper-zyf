#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 06:15:35 2017

@author: zhaoy
"""
import os
import os.path as osp

import requests

from qiniu import Auth
from qiniu import BucketManager

from ak_sk import get_ak_sk


access_key, secret_key = get_ak_sk()

download_save_path = r'./'
if not osp.exists(download_save_path):
    os.makedirs(download_save_path)

OVERWRITE_LOCAL_FILE = False


bucket_name = 'facex-train-sphereface-bs256-0807'
bucket_domain = 'http://oubom5rzl.bkt.clouddn.com'
#prefix = 'lfw'
prefix = None

#contains_str = None
contains_str = '.caffemodel'


#初始化Auth状态
q = Auth(access_key, secret_key)
#初始化BucketManager
bktMgr = BucketManager(q)
#你要测试的空间， 并且这个key在你空间中存在

print '===> Get key list (i.e. file list) in bucket %s <===' % bucket_name

#获取文件的状态信息
ret = bktMgr.list(bucket_name, prefix)

items = ret[0]['items']
#print items

if contains_str:
    key_list = [it['key'] for it in items if contains_str in it['key'].lower()]
else:
    key_list = [it['key'] for it in items]

key_list.sort()

print key_list
#
print '===> Start downloading <==='

for key in key_list:
    #有两种方式构造base_url的形式
    if '28' not in key:
        continue

    save_fn = osp.join(download_save_path, key)
    if not OVERWRITE_LOCAL_FILE and osp.exists(save_fn):
        print '---> File already exists, will not download this one'
        continue

    base_url = 'http://%s/%s' % (bucket_domain, key)
    print '---> download url: ' + base_url
    #可以设置token过期时间
    private_url = q.private_download_url(base_url)
    print '---> private_url: ' + private_url
    r = requests.get(private_url)

    if r.status_code == 200:
        print 'requests.get(private_url) ---> Succeeded'

        fp = open(save_fn, 'wb')
        fp.write(r)
        fp.close()
    else:
        print 'requests.get(private_url) ---> Failed'
