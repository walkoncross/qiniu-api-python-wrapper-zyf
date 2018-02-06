#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 19:01:49 2017

@author: zhaoy
"""
from advanced_operations import advanced_move_all


if __name__ == '__main__':
    ##################################################
    # configs
    aksk_config = './ak_sk.json'
    bucket = 'face-recog-sphereface-vggface2'
    bucket2 = bucket
    #prefix = 'lfw'
    prefix = '/'

    max_list_cnt = None
    contain_str_list = None
    #contain_str_list2 = 'celeb'
    contain_str_list2 = None

    ##################################################

    ##################################################
    # generate key in bucket2
    # def get_new_key(key):
    #     return key

    def get_new_key(key):
        #    new_key = key.replace('sphereface-64-prototxt', 'train-results')
        #    new_key = 'eval-results/' + key
        #    new_key = key.replace('resultss', 'results/s')
        new_key = key[1:]
        return new_key
    ##################################################

    advanced_move_all(aksk_config, bucket, prefix,
                      bucket2, get_new_key,
                      max_list_cnt,
                      contain_str_list, contain_str_list2
                      )
