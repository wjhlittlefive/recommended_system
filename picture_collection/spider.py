#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
单线程图片爬虫
使用 requests
'''
import requests
from lxml import etree
import time

ROOT_URL = 'https://www.zhihu.com/topic/19776749/hot'
ALLOW_DOMAIN = "zhihu.com"

def fetch_page(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            time.sleep(60)
    except:
        pass

def get_picture_url(page):
    selector = etree.HTML(page)
    urls = selector.xpath('//img/@src')
    return urls

def store_data(data):
    pass

def main():

