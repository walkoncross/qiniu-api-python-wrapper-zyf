#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""

from advanced_operations import advanced_list_all


if __name__=='__main__':
    ##################################################
    # configs
    aksk_config = './ak_sk.json'

    bucket = 'face-megaface-eval'
    #prefix = 'lfw'
    prefix = 'eval-results/'
    max_list_cnt = None

    contain_str_list = None
    #contain_str_list = ['.zip', '.tgz', '.tar.gz', '.whl', 'sh']
    #contain_str_list = ['.mat']
    contain_str_list2 = ['']
    #contain_str_list2 = ['lfw']

    save_dir = './rlt_list_bucket'
    save_details = False
    ##################################################

    advanced_list_all(aksk_config,
                        bucket, prefix,
                        max_list_cnt,
                        contain_str_list, contain_str_list2,
                        save_dir,
                        save_details)