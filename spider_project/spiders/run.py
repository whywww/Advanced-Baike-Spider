# coding:utf-8
from scrapy import cmdline
cmdline.execute("scrapy crawl BaikeSpider -o baike.json".split())