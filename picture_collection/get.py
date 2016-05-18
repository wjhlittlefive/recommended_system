#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
为图片贴标签
单线程
'''

import requests
import json

def get_sha256sum(request_url, post_url=None):
    payload = {'url': "https://upload.wikimedia.org/wikipedia/commons/8/85/Garden_bench_001.jpg"}
    try:
        response = requests.post(url=request_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'}, timeout=5)
        if response.status_code == 200:
            return response.json()['sha256sum']
    except:
        pass

if __name__ == "__main__":
    print(get_sha256sum('http://127.0.0.1:5000/addURL'))
