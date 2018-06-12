#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""
from qiniu_api_wrapper import advanced_move_all
import os.path as osp


if __name__ == '__main__':
    ##################################################
    # configs
    aksk_config = './ak_sk.json'
    bucket = 'face-insight'
    bucket2 = bucket
    #prefix = 'lfw'
    prefix = 'train-logs/rlt_parse_log-train-log'

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

    ##################################################
    # generate key in bucket2
    # def get_new_key(key):
    #     return key

    def get_new_key(key):
        #    new_key = key.replace('sphereface-64-prototxt', 'train-results')
        #    new_key = 'eval-results/' + key
        new_key = key.replace('rlt_parse_log-train-log', 'rlt-parse-train-log')
#        new_key = key[1:]
#        new_key = key.replace('idcard1M-features-', '')
#        new_key = 'eval-results/insightface-r100-ms1m-zyf-0221-ep80/' + key
#        new_key = key.replace('cmc', 'eval-results/insightface-r100-ms1m-zyf-0221-ep80/cmc')

        return new_key
    ##################################################

    advanced_move_all(aksk_config, bucket, prefix,
                      bucket2, get_new_key,
                      max_list_cnt,
                      contain_str_list, contain_str_list2
                      )
