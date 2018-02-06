#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""

from advanced_operations import advanced_delete_all


if __name__ == '__main__':

    ##################################################
    # configs
    aksk_config = './ak_sk.json'

    bucket = 'face-webface2'
    #prefix = 'lfw'
    prefix = 'CASIA-aligned/'
    max_list_cnt = 50

    contain_str_list = None
    #contain_str_list = ['.bin']
    #contain_str_list = ['.zip', '.tgz', '.tar.gz', '.whl', 'sh']
    # contain_str_list = ['log_1007_2.txt', 'extract-log']
    contain_str_list2 = None
    #contain_str_list2 = ['.bin']
    #contain_str_list2 = ['lfw']
    ##################################################

    advanced_delete_all(aksk_config, bucket, prefix,
                        max_list_cnt, contain_str_list, contain_str_list2
                        )
