#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""

from qiniu_api_wrapper import advanced_delete_all


if __name__ == '__main__':

    ##################################################
    # configs
    aksk_config = './ak_sk.json'

    bucket = 'face-megaface-eval'
    #prefix = 'lfw'
#    prefix = 'CASIA-aligned/'
    prefix = 'eval-resultsL'
    max_list_cnt = None

    contain_str_list = None
#    contain_str_list = ['ch', 'co', 'me', 'ad', 'ls']
#    contain_str_list = ['insightface-r100-ms1m-zyf-0221-ep80']
    #contain_str_list = ['.zip', '.tgz', '.tar.gz', '.whl', 'sh']
    # contain_str_list = ['log_1007_2.txt', 'extract-log']
    contain_str_list2 = None
    #contain_str_list2 = ['.bin']
    #contain_str_list2 = ['lfw']
    ##################################################

    advanced_delete_all(aksk_config, bucket, prefix,
                        max_list_cnt, contain_str_list, contain_str_list2
                        )
