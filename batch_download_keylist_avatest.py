#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 06:15:35 2017

@author: zhaoy
"""
from advanced_operations import advanced_download_keylist


if __name__ == '__main__':

    ##################################################
    # configs
    aksk_config = './ak_sk_avatest.json'

    bucket_domain = 'http://p4rahjzrc.bkt.clouddn.com'
    key_list = './lego-raw_key_list.txt'
    # key_list = ['1.jpg', '2.jpg']

    download_save_path = r'D:\face-databases\lego-hotel-faces'
    overwrite_local_file = False
    download_expire_time = 3600
    ##################################################

    advanced_download_keylist(key_list,
                              aksk_config,
                              bucket_domain,
                              download_save_path,
                              download_expire_time,
                              overwrite_local_file)
