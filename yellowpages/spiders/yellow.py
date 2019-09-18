# -*- coding: utf-8 -*-
import scrapy

from scrapy.contrib.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from yellowpages.items import *
items = []

## call this script in bash
##scrapy runspider yellow.py -a category=plumbing  -a location=ontario -o plumbing-ontario.csv -t csv

class LanacionSpider(scrapy.Spider):
    name = 'yellowpages'

    def __init__(self, category='',location='', **kwargs):
        super(LanacionSpider, self).__init__(**kwargs)
        self.start_urls = ['https://www.yellowpages.com/search?search_terms='+category+'&geo_location_terms='+location+'&page=1']  # py36
       # super().__init__(**kwargs)  # python3

    allowed_domains = ['yellowpages.com']

    Rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*[contains(@class,"next ajax-page")]/a'))),
        Rule(LinkExtractor(allow=(), restrict_xpaths=('//*/div/div[2]/div[2]/h2/a')),callback="parse",follow=False)
        }

    def parse(self, response):
        item = JItem()
        global items

        item['name'] = response.xpath('//*[@id="main-header"]/article/div/h1/text()').extract()
        item['address'] = response.xpath('//*[@id="main-header"]/article/section[2]/div[1]/p[1]/span/text()').extract()
        item['phone'] = response.xpath('//*/article/section[2]/div[1]/p[2]/text()').extract()
        item['image'] =""
        if ('//*[@id="gallery"]/div[2]/div/a/img/@src'):
            item['image'] = response.xpath('//*[@id="gallery"]/div[2]/div/a/img/@src').extract()

        item['email']= response.xpath('//*[contains(@class,"email-business")]/@href').extract()
        item['website'] = response.xpath('//*[contains(@class,"links")]/@href').extract()
        item['logo']=""
        if response.xpath('//*[@id="business-info"]/dl/dd[2]/img/@src').extract():
            item['logo']= response.xpath('//*[@id="business-info"]/dl/dd[2]/img/@src').extract()
        ##print(response.xpath('//*[@id="main-header"]/article/section[2]/div[1]/p[1]/span/text()').extract())
        next_page = response.xpath('//*[contains(@class,"next ajax-page")]/@href').extract()
        if next_page:
            next_href = next_page[0]
            #print(next_href)
            next_page_url = 'https://www.yellowpages.com' + next_href
            request = scrapy.Request(url=next_page_url)
            ##print   "entro aca hacer pag siguiente"
            yield request

        datas= response.xpath('//*/div/div[2]/div[2]/h2/a/@href').extract()
        for next_href in datas:
            ##print(next_href)
            next_page_url = 'https://www.yellowpages.com' + next_href
            request = scrapy.Request(url=next_page_url)
            ##print "entro aca hacer pag siguiente data"
            yield request

        yield item




