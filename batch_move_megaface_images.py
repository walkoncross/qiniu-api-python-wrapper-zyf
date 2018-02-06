#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""
from advanced_operations import advanced_download_all


if __name__ == '__main__':

    ##################################################
    # configs
    aksk_config = './ak_sk_avatest.json'

    bucket = 'identities-dataset'
    bucket2 = 'face-megaface-images'
    #prefix = 'Celeb'
    prefix = 'assets/megaface/identities_all/'

    prefix_len = len(prefix)

    max_list_cnt = None

    contain_str_list = None
    #contain_str_list = ['.zip', '.tgz', '.tar.gz', '.whl', 'sh']
    # contain_str_list = ['.mat']
    contain_str_list2 = ['']
    # contain_str_list2 = ['lfw']
    ##################################################
    
    advanced_move_all(aksk_config, bucket, prefix,
                      bucket2, get_new_key,
                      max_list_cnt,
                      contain_str_list, contain_str_list2
                      )