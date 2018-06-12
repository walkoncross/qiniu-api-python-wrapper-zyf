#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 06:08:07 2018

@author: zhaoy
"""
from qiniu_api_wrapper import advanced_move_all


if __name__ == '__main__':
    ##################################################
    # configs
    aksk_config = './ak_sk.json'
    bucket = 'face-recog-thresholds'
    bucket2 = 'face-model-thresholds'
    #prefix = 'Celeb'
    prefix = ''

    prefix_len = len(prefix)

    max_list_cnt = None

    contain_str_list = None
    #contain_str_list = ['.zip', '.tgz', '.tar.gz', '.whl', 'sh']
#    contain_str_list = ['.zip']
    contain_str_list2 = None
    # contain_str_list2 = ['lfw']
    ##################################################

    def get_new_key(key):
        #    new_key = key[prefix_len:]
        new_key = key
        return new_key

    advanced_move_all(aksk_config, bucket, prefix,
                      bucket2, get_new_key,
                      max_list_cnt,
                      contain_str_list, contain_str_list2
                      )