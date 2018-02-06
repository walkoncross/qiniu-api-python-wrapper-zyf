#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""

from qiniu import Auth
from qiniu import BucketManager

import json
import codecs

from ak_sk import get_ak_sk


from advanced_operations import advanced_list_all


if __name__ == '__main__':
    ##################################################
    # configs
    aksk_config = './ak_sk_avatest.json'
    save_details = False

    bucket = 'identities-dataset'
    #prefix = 'lfw'
    #prefix = None
    prefix = 'assets/face_card_data'
    max_list_cnt = None  # set to None for no limit
    #contain_str_list = None
    contain_str_list = ['.zip', '.tgz', '.tar.gz', '.txt']
    #contain_str_list2 = ['']
    contain_str_list2 = ['lfw']
    ##################################################

    advanced_list_all(aksk_config,
                      bucket, prefix,
                      max_list_cnt,
                      contain_str_list, contain_str_list2,
                      save_dir,
                      save_details)
