#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 06:08:07 2018

@author: zhaoy
"""
from qiniu_api_wrapper import advanced_upload_paths


if __name__ == '__main__':
    ##################################################
    # configs
    aksk_config = './ak_sk.json'
    bucket = 'face-data'

    # You can list all the files/folders in local_paths
    # All contents under folder will be expanded and uploaded.
    local_paths = [
        './local_file_1.txt',
        './local_file_2.txt',
        './local_folder_1',
        './local_folder_2'
    ]

    prefix = ''

    upload_expire_time = -1
    ##################################################

    advanced_upload_paths(aksk_config,
                          bucket,
                          local_paths,
                          prefix,
                          upload_expire_time)
