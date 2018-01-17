# -*- coding: utf-8 -*-
"""
@Project: 百度百科词条爬虫

@Author：魏昊妤

@Create date: 2017-12-25

@description：本项目为计算机网络课程项目

@Update date：2018-1-5
"""
import MySQLdb.cursors
import re
from scrapy.spiders import CrawlSpider, Rule
from spider_project.items import SpiderProjectItem
import logging
from scrapy.selector import Selector
import scrapy
from bs4 import BeautifulSoup
import urllib2
# p = r"<.+?>"
# pattern = re.compile(p)
db = MySQLdb.connect("127.0.0.1", "dqq", "123456", "baidu", charset="utf8")

class BaikeSpider(CrawlSpider):
    name = "BaikeSpider"
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com']

    '''
    遍历百度百科首页上的所有分类url
    '''
    def parse(self, response):
        namelist = []
        sel = Selector(response)
        classpage = sel.xpath(
            '//div[@class="column"]').extract()

        for i in range(len(classpage)):
            classname = re.findall(r'>.*?<', classpage[i]) # 爬取首页分类的列
            for num in range(len(classname)):
                st = classname[num][1:-1]
                if st == "" or st == " | ":
                    pass
                else:
                    namelist.append(classname[num][1:-1]) # 分类名的列表
        for count in range(len(namelist)): 
            url = "http://baike.baidu.com/fenlei/" + namelist[count]
            # print (url)
            yield scrapy.Request(url, callback=self.parse_onepage)

    '''
    递归爬取子分类页面上的每个词条URL
    并调用解析函数parse_item解析词条
    '''
    def parse_onepage(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        totalView = soup.find_all('a', href=re.compile(
            r'/view/.+'))
        totalFenlei = soup.find_all('a', href=re.compile(
            r'/fenlei/.+'))

        for href in totalView:
            try:
                itemUrl = "http://baike.baidu.com" + href.attrs['href']
                #print itemU
                self.parse_item(itemUrl)
            except:
                continue
        for href in totalFenlei:
            try:
                # 递归爬取
                fenleiUrl = "http://baike.baidu.com" + href.attrs['href']
                # print (itemUrl)
                yield scrapy.Request(url = fenleiUrl, callback=self.parse_onepage)
            except:
                continue

    '''
    解析词条中的内容
    '''
    def parse_item(self, response):
        try:
            page = urllib2.urlopen(response)
            text = page.read()
            soup = BeautifulSoup(text,"html.parser")

            # 爬取词条的标题名和摘要，如果还要爬取别的内容可以再加别的项
            soupTitle = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
            soupSummary = soup.find('div', class_='lemma-summary').get_text()

            baike_item = SpiderProjectItem()
            baike_item['itemTitle'] = soupTitle
            baike_item['itemUrls'] = response
            baike_item['itemSummary'] = soupSummary

            cursor = db.cursor()
            cursor.execute('insert into items values("%s","%s","%s")' % (baike_item['itemTitle'], baike_item['itemUrls'], baike_item['itemSummary']))
            db.commit()

            return baike_item
        except:
            logging.error()


