#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 06:15:35 2017

@author: zhaoy
"""
from qiniu_api_wrapper import advanced_download_all


if __name__ == '__main__':

    ##################################################
    # configs
    aksk_config = './ak_sk.json'

    bucket = 'face-asian'
    bucket_domain = 'http://xxxxx.bkt.clouddn.com'
    prefix = 'face_asian'

    max_list_cnt = 10
    contain_str_list = None
    contain_str_list2 = None
    #contain_str_list = 'txt'

    download_save_path = r'./bkt_download_files/face-asian'
    overwrite_local_file = False
    download_expire_time = 3600
    ##################################################
    advanced_download_all(aksk_config,
                          bucket, bucket_domain,
                          prefix,
                          max_list_cnt,
                          contain_str_list,
                          contain_str_list2,
                          download_save_path,
                          download_expire_time,
                          overwrite_local_file)
