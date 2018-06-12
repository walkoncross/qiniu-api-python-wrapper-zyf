# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 18:58:22 2017

@author: zhaoy
"""
import json
import os.path as osp


def get_ak_sk(json_file=None):
    if json_file is None:
        json_file = osp.join(osp.dirname(__file__), 'ak_sk.json')

    if not osp.exists(json_file):
        raise Exception('Cound not found ak_sk json file: ' + json_file)

    fd = open(json_file, 'r')
    ak_sk = json.load(fd)
    fd.close()

    return ak_sk["access_key"], ak_sk["secret_key"]

if __name__=='__main__':
    ak, sk = get_ak_sk()
    print 'ak: %s\nsk:%s' % (ak, sk)