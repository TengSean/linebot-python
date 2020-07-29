import scrapy
from scrapy_splash import SplashRequest, SplashFormRequest

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


# from tutorial.items import Stock_Price
# from tutorial.richLogging import RL

import os, time

class price_item(scrapy.Item):
    file_url = scrapy.Field()
    file = scrapy.Field()

class Stock_Price(scrapy.Spider):
    name = 'stock_price'
    # rl = RL()

    def start_requests(self, ):
        base_urls = [
            # 'https://query1.finance.yahoo.com/v7/finance/download/'
            'https://query1.finance.yahoo.com/v7/finance/download/2330?period1=1514764800&period2=1551312000&interval=1d&events=history'
        ]

        # self.ticker
        # self.period1
        # self.period2
        # self.rl.debug('This testing')
        for url in base_urls:
            yield scrapy.Request(
                                url,
                                headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'},
                                callback=self.parse
                                )
            # yield SplashRequest(url,
            #             self.parse,
            #             )

    def parse(self, response):
        with open('./this_is_test.csv', 'wb') as f:
            f.write(response.body)



# configure_logging()
# runner = CrawlerRunner()
# @defer.inlineCallbacks
# def crawl():
#     yield runner.crawl(Stock_Price)
#     reactor.stop()

# crawl()
# reactor.run()