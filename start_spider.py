from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
import json
import os

keywords_file = '../keywords/keywords_20170906.json'
with open(keywords_file, 'r') as f:
    lines = json.load(f)
    for key, values in lines.items():
        for keyword in values:
            bing_crawler = BingImageCrawler(downloader_threads=4,
                                            storage={'root_dir': '../images/'+ key})
            bing_crawler.crawl(keyword=keyword, offset=0, max_num=1000,
                                min_size=None, max_size=None)

#baidu_crawler = BaiduImageCrawler(storage={'root_dir': './images'})
#baidu_crawler.crawl(keyword='sunny', offset=0, max_num=1000,
#                   min_size=None, max_size=None)
