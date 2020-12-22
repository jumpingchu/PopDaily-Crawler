#!/usr/bin/env python
# coding: utf-8

import requests
import re

def get_latest_urls(page_url, page_types):
    resp = requests.get(page_url)
    pattern = r'(?<=,\"url\":\")https://www.popdaily.com.tw/{}/\d+'.format(page_types)
    if resp.status_code == 200:
        urls = re.findall(pattern , resp.text)
    return urls

def urls_process(sitemap_url):
    resp = requests.get(sitemap_url)
    if resp.status_code == 200:
        urls = re.findall(r'<loc>(https:.+)</loc>', resp.text)
        skip_list = ['topic', 'trend', 'forum']
        PGC_urls = [url for url in urls if all(skip not in url for skip in skip_list)]
     
    print('總篇數: ', len(urls))
    print('PGC 文章篇數', len(PGC_urls))
    
    return PGC_urls

def url_classify(original_urls, latest_urls):
    urls_dict = {
        'japan': [], 
        'travel': [],  
        'food': [], 
        'life': [], 
        'press': [],
        'other': []
    }

    for url in original_urls:
        if 'japan' in url:
            urls_dict['japan'].append(url)
        elif 'travel' in url:
            urls_dict['travel'].append(url)
        elif 'food' in url:
            urls_dict['food'].append(url)
        elif 'life' in url:
            urls_dict['life'].append(url)
        elif 'press' in url:
            urls_dict['press'].append(url)
        else:
            urls_dict['other'].append(url)
    
    for type_ in page_types:
        urls_dict[type_] += [url for url in latest_urls[type_] if url not in urls_dict[type_]]
    
    article_counts = 0
    for i in urls_dict:
        print('分類', i.upper(), '有', len(urls_dict[i]), '個連結')
        article_counts += len(urls_dict[i])
    print('總共', article_counts, '個連結')
    
    return urls_dict

base_url = 'https://www.popdaily.com.tw/'
page_types = ['japan', 'travel', 'food', 'life', 'press']

latest_urls = {}
for page in page_types:
    latest_urls[page] = get_latest_urls(base_url+page, page)

sitemap = 'https://www.popdaily.com.tw/sitemaps/post/page/440000'

PGC_urls = urls_process(sitemap)

urls_dict = url_classify(PGC_urls, latest_urls)

if __name__ == "__main__":
    pass

