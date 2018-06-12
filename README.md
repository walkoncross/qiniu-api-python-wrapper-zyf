# qiniu-api-python-wrapper-zyf
This python wrapper is aimed to do some conditional operations in batch with the qiniu cloud api.

You can select files (or bucket keys in qiniu cloud) with two 'embedded' select conditions. You can list/delete/rename bucket keys, modify prefix of keys in qiniu cloud buckets, upload local paths (both folders and files) into, download files from qiniu cloud buckets.

Support both public and private buckets.

## Requirements
```cmd
pip install requests qiniu 
```

## Usage:
1. Put your qiniu ak/sk into ak_sk.json;
2. Run batch*.py or list*.py as you need. (Make some configs in these *.py according to your need)
