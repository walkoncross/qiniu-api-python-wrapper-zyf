# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 06:28:43 2018

@author: zhaoy
"""
import os
import os.path as osp

import codecs
import json

import requests

from qiniu import Auth
from qiniu import BucketManager

from ak_sk import get_ak_sk


def get_qiniu_auth(aksk_config=None, access_key=None, secret_key=None):
    if aksk_config:
        if isinstance(aksk_config, str):
            ak, sk = get_ak_sk(aksk_config)
        else:
            ak = aksk_config['access_key']
            sk = aksk_config['secret_key']
    else:
        ak = access_key
        sk = secret_key

    print 'ak: ', ak
    print 'sk: ', sk

    # 初始化Auth状态
    auth = Auth(ak, sk)

    return auth


def get_bucket_manager(aksk_config=None,
                       access_key=None, secret_key=None,
                       auth=None):
    if auth is None:
        auth = get_qiniu_auth(aksk_config, access_key, secret_key)

    # 初始化BucketManager
    bkt_mgr = BucketManager(auth)

    return bkt_mgr


def advanced_list_all(aksk_config,
                      bucket, prefix,
                      max_list_cnt=None,
                      contain_str_list=None,
                      contain_str_list2=None,
                      save_dir=None,
                      save_details=False,
                      access_key=None, secret_key=None):
    '''
    ##################################################
    # configs
    save_dir='./'
    save_details = False

    bucket = 'face-megaface-eval'
    #prefix = 'lfw'
    prefix = 'eval-results/'
    max_list_cnt = None

    contain_str_list = None
    #contain_str_list = ['.zip', '.tgz', '.tar.gz', '.whl', 'sh']
    #contain_str_list = ['.mat']
    contain_str_list2 = ['']
    #contain_str_list2 = ['lfw']
    ##################################################
    '''
    if save_dir is None:
        save_dir = './'
    elif not osp.exists(save_dir):
        os.makedirs(save_dir)

    rlt_list_file = osp.join(save_dir, bucket + '_key_list.txt')
    fp = codecs.open(rlt_list_file, 'w', encoding='utf-8')

    if save_details:
        rlt_list_file2 = osp.join(
            save_dir, bucket + '_key_list_details.json')
        fp2 = codecs.open(rlt_list_file2, 'w', encoding='utf-8')
        fp2.write('[\n')

    bkt_mgr = get_bucket_manager(aksk_config, access_key, secret_key)

    marker = None
    while True:
        # 获取文件的状态信息
        ret = bkt_mgr.list(bucket, prefix, marker, max_list_cnt)

        if not ret[0]:
            print "No qualified files in the bucket"
            break

        items = ret[0]['items']

        if contain_str_list:
            #        key_list = [it['key']
            #                    for it in items if contain_str_list in it['key'].lower()]
            #        if save_details:
            #            key_list_detail = [
            # it for it in items if contain_str_list in it['key'].lower()]
            key_list = []
            key_list_detail = []
            for i in range(len(items)):
                for sub_str in contain_str_list:
                    if sub_str in items[i]['key'].lower():
                        key_list.append(items[i]['key'])
                        if save_details:
                            key_list_detail.append(items[i])
                        break
        else:
            key_list = [it['key'] for it in items]
            if save_details:
                key_list_detail = [it for it in items]

        if contain_str_list2:
            key_list_2 = []
            key_list_detail_2 = []
            for i in range(len(key_list)):
                for sub_str in contain_str_list2:
                    if sub_str in key_list[i].lower():
                        key_list_2.append(key_list[i])
                        if save_details:
                            key_list_detail_2.append(items[i])
                        break

            key_list = key_list_2
            if save_details:
                key_list_detail = key_list_detail_2

        # print key_list
        fetch_cnt = len(key_list)
        print "%d qualified files found" % fetch_cnt

        first_n = min(fetch_cnt, 10)
        print "---> First %d files:" % first_n
        for i in range(first_n):
            print '%d --> %s' % (i + 1, key_list[i])

        #json.dump(key_list, fp, indent=2)

        for it in key_list:
            fp.write(it + '\n')

        if save_details:
            #        json.dump(key_list_detail, fp2, indent=2)
            for it in key_list_detail:
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

    return key_list


def default_new_key_func(key):
    new_key = key

    return new_key


def advanced_move_all(aksk_config,
                      bucket, prefix,
                      bucket2, new_key_func=None,
                      max_list_cnt=None,
                      contain_str_list=None,
                      contain_str_list2=None,
                      access_key=None, secret_key=None):
    '''
    ##################################################
    # configs
    #save_details = False
    #
    #bucket = 'face-webface2'
    ##prefix = 'lfw'
    #prefix = 'CASIA-aligned/'
    #max_list_cnt = None
    #
    #contain_str_list = None
    ##contain_str_list = ['.bin']
    ##contain_str_list = ['.zip', '.tgz', '.tar.gz', '.whl', 'sh']
    ## contain_str_list = ['log_1007_2.txt', 'extract-log']
    #contain_str_list2 = None
    #contain_str_list2 = ['.bin']
    #contain_str_list2 = ['lfw']
    ##################################################
    '''
    suc_cnt = 0
    fail_cnt = 0

    if new_key_func is None:
        get_new_key = default_new_key_func
    else:
        get_new_key = new_key_func

    bkt_mgr = get_bucket_manager(aksk_config, access_key, secret_key)

    marker = None
    while True:
        # 获取文件的状态信息
        ret = bkt_mgr.list(bucket, prefix, marker, max_list_cnt)

        if not ret[0]:
            print "No qualified files in the bucket"
            break

        items = ret[0]['items']

        if contain_str_list:
            #        key_list = [it['key']
            #                    for it in items if contain_str_list in it['key'].lower()]
            #        if save_details:
            #            key_list_detail = [
            # it for it in items if contain_str_list in it['key'].lower()]
            key_list = []
            for i in range(len(items)):
                for sub_str in contain_str_list:
                    if sub_str in items[i]['key'].lower():
                        key_list.append(items[i]['key'])
                        break
        else:
            key_list = [it['key'] for it in items]

        if contain_str_list2:
            key_list_2 = []
            for i in range(len(key_list)):
                for sub_str in contain_str_list2:
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
            ret2 = bkt_mgr.move(bucket, key, bucket2, key2)
            print '\n===> Moving {} into {}'.format(
                osp.join(bucket, key), osp.join(bucket2, key2)
            )
            if ret2:
                print '---> Failed to move'
                print '---> bucket.move() returns:'
                print ret2
                fail_cnt += 1
            else:
                print '---> Succeeded to move'
                suc_cnt += 1

        if 'marker' in ret[0]:
            print 'Returned marker is: ', marker
            print 'More files to list'
            marker = ret[0]['marker']

            if max_list_cnt:
                max_list_cnt = max_list_cnt - fetch_cnt
        else:
            print 'No more files, list fininshed'
            break

    print '===> Succeeded to move %d files' % suc_cnt
    print '===> Failed to move %d files' % fail_cnt


def advanced_delete_all(aksk_config,
                        bucket, prefix,
                        max_list_cnt=None,
                        contain_str_list=None,
                        contain_str_list2=None,
                        access_key=None, secret_key=None):

    cnt = 0

    bkt_mgr = get_bucket_manager(aksk_config, access_key, secret_key)

    marker = None
    while True:
        # 获取文件的状态信息
        ret = bkt_mgr.list(bucket, prefix, marker, max_list_cnt)

        if not ret[0]:
            print "===> No qualified files in the bucket"
            break

        items = ret[0]['items']

        if contain_str_list:
            #        key_list = [it['key']
            #                    for it in items if contain_str_list in it['key'].lower()]
            #        if save_details:
            #            key_list_detail = [
            # it for it in items if contain_str_list in it['key'].lower()]
            key_list = []

            for i in range(len(items)):
                for sub_str in contain_str_list:
                    if sub_str in items[i]['key'].lower():
                        key_list.append(items[i]['key'])
                        break
        else:
            key_list = [it['key'] for it in items]

        if contain_str_list2:
            key_list_2 = []

            for i in range(len(key_list)):
                for sub_str in contain_str_list2:
                    if sub_str in key_list[i].lower():
                        key_list_2.append(key_list[i])
                        break

            key_list = key_list_2

        # print key_list
        fetch_cnt = len(key_list)
        print "\n===> %d qualified files found" % fetch_cnt

        first_n = min(fetch_cnt, 10)
        print "---> First %d files:" % first_n
        for i in range(first_n):
            print '%d --> %s' % (i + 1, key_list[i])

        for it in key_list:
            print '---> delete ', it
            bkt_mgr.delete(bucket, it)
            cnt += 1
            print '\n===> %d files deleted\n' % cnt

        if 'marker' in ret[0]:
            print '\n===> Returned marker is: ', marker
            print '       More files to list'
            marker = ret[0]['marker']

            if max_list_cnt:
                max_list_cnt = max_list_cnt - fetch_cnt
        else:
            print '\n===> No more files, list fininshed'
            break


def advanced_download_all(aksk_config,
                          bucket, bucket_domain,
                          prefix,
                          max_list_cnt=None,
                          contain_str_list=None,
                          contain_str_list2=None,
                          download_save_path=None,
                          download_expire_time=-1,
                          overwrite_local_file=False,
                          access_key=None, secret_key=None):
    '''
    ##################################################
    # configs

    #bucket = 'facex-train-sphereface-bs256-0807'
    #bucket_domain = 'http://oubom5rzl.bkt.clouddn.com'
    #prefix = 'lfw'
    #prefix = None

    bucket = 'face-asian'
    bucket_domain = 'http://outj1l7fd.bkt.clouddn.com'
    prefix = 'face_asian'

    contain_str_list = None
    #contain_str_list = 'txt'
    ##################################################
    '''
    if not download_save_path:
        download_save_path = r'./bkt_download_files'

    if not osp.exists(download_save_path):
        os.makedirs(download_save_path)

    if download_expire_time <= 0:
        download_expire_time = 3600

    # bkt_mgr = get_bucket_manager(aksk_config, access_key, secret_key)

    q_auth = get_qiniu_auth(aksk_config, access_key, secret_key)
    bkt_mgr = get_bucket_manager(auth=q_auth)

    marker = None
    while True:
        # 获取文件的状态信息
        ret = bkt_mgr.list(bucket, prefix, marker, max_list_cnt)

        if not ret[0]:
            print "No qualified files in the bucket"
            break

        items = ret[0]['items']

        if contain_str_list:
            #        key_list = [it['key']
            #                    for it in items if contain_str_list in it['key'].lower()]
            #        if save_details:
            #            key_list_detail = [
            # it for it in items if contain_str_list in it['key'].lower()]
            key_list = []

            for i in range(len(items)):
                for sub_str in contain_str_list:
                    if sub_str in items[i]['key'].lower():
                        key_list.append(items[i]['key'])
                        break
        else:
            key_list = [it['key'] for it in items]

        if contain_str_list2:
            key_list_2 = []

            for i in range(len(key_list)):
                for sub_str in contain_str_list2:
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
            # 有两种方式构造base_url的形式
            #    if '28' not in key:
            #        continue
            #
            # makedirs for key in the form "xxx/yyy/zzz"
            if '/' in key:
                osp.makedirs(osp.join(download_save_path, osp.split(key)[0]))

            save_fn = osp.join(download_save_path, key)
            if not overwrite_local_file and osp.exists(save_fn):
                print '---> File already exists, will not download this one'
                continue

            if not bucket_domain.startswith('http'):
                base_url = 'http://%s/%s' % (bucket_domain, key)
            else:
                base_url = '%s/%s' % (bucket_domain, key)

            print '---> download url: ' + base_url
            # 可以设置token过期时间
            private_url = q_auth.private_download_url(
                base_url, download_expire_time)
            print '---> private_url: ' + private_url
            r = requests.get(private_url)

            if r.status_code == 200:
                print 'requests.get(private_url) ---> Succeeded'

                fp = open(save_fn, 'wb')
                fp.write(r.content)
                fp.close()
            else:
                print 'requests.get(private_url) ---> Failed'

            r.close()

        if 'marker' in ret[0]:
            print 'Returned marker is: ', marker
            print 'More files to list'
            marker = ret[0]['marker']

            if max_list_cnt:
                max_list_cnt = max_list_cnt - fetch_cnt
        else:
            print 'No more files, list fininshed'
            break