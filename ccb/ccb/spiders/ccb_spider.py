#!/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log
from ccb.items import CcbItem
from urlparse import urljoin
from scrapy.http import Request
import re


class CcbSpider(Spider):

    name = "wooyun"
    allowed_domains = ["wooyun.org"]
    start_urls = [
        "http://www.wooyun.org/bugs/",
        "http://www.wooyun.org/bugs/page/2"
    ]
    #填写需要过滤的网址
    def parse(self, response):

        sel = Selector(response)
        sites = sel.xpath('/html/body/div[5]/table[3]/tbody/tr')

        for site in sites:

            title = site.xpath('td/a/text()').re(ur'.*\u4e2d\u56fd.*')  #此处输入过滤关键字的unicode编码，如此处过滤“中国”

            if title:
                url_before_bind = site.xpath('td/a/@href').extract()
                wooyunurl = "http://www.wooyun.org" + url_before_bind[0]

                yield Request(wooyunurl, callback=self.second_parse)

            #记录
            log.msg("Appending item...",level='INFO')


        log.msg("Append done.",level='INFO')

    def second_parse(self,response):

        content = Selector(response)

        title = content.xpath('//div[@class="content"]/h3[2]/text()').extract()
        submit_time = content.xpath('//div[@class="content"]/h3[5]/text()').extract()
        level = content.xpath('//div[@class="content"]/h3[8]/text()').extract()
        item = CcbItem()
        item['title'] = [t.encode('utf-8') for t in title]
        item['submit_time'] = [l.encode('utf-8') for l in submit_time]
        item['level'] = [le.encode('utf-8') for le in level]
        yield item
        log.msg("Appending fff item...",level='INFO')
