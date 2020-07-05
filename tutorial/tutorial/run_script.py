# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

# from scrapy_selenium import SeleniumRequest
from bs4 import BeautifulSoup
# import middlewares

from scrapy_splash import SplashRequest, SplashFormRequest
import os, time

import pandas as pd
import numpy as np

# from scrapy.utils.project import get_project_settings

class mySpyder(scrapy.Spider):
    name = 'spyder1'

    custom_settings = {
        "SPIDER_MIDDLEWARES" : {
            'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,   
        },
        "DOWNLOADER_MIDDLEWARES" : {
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
        },

        "SPLASH_URL" : 'http://localhost:8050',
        "DUPEFILTER_CLASS" : 'scrapy_splash.SplashAwareDupeFilter',
        "HTTPCACHE_STORAGE" : 'scrapy_splash.SplashAwareFSCacheStorage'
    }

    def start_requests(self, ):
        urls = [
            'https://mops.twse.com.tw/mops/web/STAMAK03_1',
            # 'http://quotes.toscrape.com/login',
            # 'https://www.google.com.tw/search?q=柯基&tbm=isch'
        ]

        lua = '''
        function main(splash, args)
            assert(splash:go(splash.args.url))
            assert(splash:wait(0.1))

            splash:select("input[id='co_id']"):send_text("2330")
            splash:select("input[id='b_date']"):send_text("1060701")
            splash:select("input[id='e_date']"):send_text("1090630")
            splash:select("input[value=' 查詢 ']"):mouse_click()
            splash:wait(3)

            return {html=splash:html()}
        end
        '''

        for url in urls:
            yield SplashRequest(url, 
                                self.parse,
                                endpoint = 'execute',
                                args = {
                                    'lua_source': lua
                                    }
                                )
        
    def parse(self, response):
        self.log('start parsing response')
        # self.log(response.text)
        for table in response.selector.xpath('//table[@class="hasBorder"]'):
            selector_list = table.xpath('//tr[@class="odd"]/td/text()|//tr[@class="even"]/td/text()')
            for i in range(0,len(selector_list), 12):
                ticker = str(selector_list[i].get().strip(' '))
                company = str(selector_list[i+1].get().strip(' '))
                identity = str(selector_list[i+3].get().strip(' '))
                name = str(selector_list[i+4].get().strip(' '))
                transaction_date = str(selector_list[i + 5].get().strip(' '))
                mortgage = str(selector_list[i + 6].get().strip(' '))
                redemption = str(selector_list[i + 7].get().strip(' '))
                cumulative_stock = str(selector_list[i + 8].get().strip(' '))
                pledgee = str(selector_list[i + 9].get().strip(' '))
                memo = str(selector_list[i + 10].get())
                declaration_date = selector_list[i + 11].get()

                # self.log(selector_list[i].get())
                self.log(f'ticker: {ticker}, company: {company}, identity: {identity}, name: {name}, transaction_date: \
                    {transaction_date}, mortgage: {mortgage}, redemption: {redemption}, cumulative_stock: {cumulative_stock}, \
                        pledgee: {pledgee}, memo: {memo}, delcartion_date: {declaration_date}')
                # self.log(identity+' '+name+' '+str(selector_list[i+11].get()))



            # for td in enumerate(table.xpath('//tr[@class="odd"]/td/text()|//tr[@class="even"]/td/text()')):
            #     self.log(td.get())
            #     v = td.get().strip(' ')
            #     # self.log('='*10)
            #     # self.log(td.get())

            #     self.log(str(v)+'====')
            #     self.log(len(v))
                # if v == ' ':
                #     self.log(v)
                #     self.log(len(v))




    def parse_login(self, response):
        self.log(response.text)
        # for q in response.css('div.quote'):
        #     yield {
        #         'author_name' : q.css('small.author::text').extract_first(),
        #         'author_url' : q.css(
        #             'small.author ~ a[href*="goodreads.com"]::attr(href)'
        #         ).extract_first()
        #     }



configure_logging()
runner = CrawlerRunner()
@defer.inlineCallbacks
def crawl():
    yield runner.crawl(mySpyder)
    reactor.stop()

crawl()
reactor.run()