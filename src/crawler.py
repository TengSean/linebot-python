# %%

import scrapy
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy_selenium import SeleniumRequest
from bs4 import BeautifulSoup

# from scrapy.utils.project import get_project_settings

class mySpyder(scrapy.Spider):
    name = 'spyder1'

    def start_requests(self, ):
        urls = [
            # 'http://quotes.toscrape.com/page/1/',
            'https://www.google.com.tw/search?q=柯基&tbm=isch'
        ]
        for url in urls:
            # yield SeleniumRequest(url=url, callback=self.parse)

            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        print(soup.prettify())

        # self.log(dir(self))
        # self.log(dir(response.request))
        # print(response.url)
        # page = response.url.split('/')[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

#%%
# configure_logging()
# runner = CrawlerRunner()
# runner.crawl(mySpyder)
# d = runner.join()
# d.addBoth(lambda _: reactor.stop())
# reactor.run()

# %%
configure_logging()
runner = CrawlerRunner()
@defer.inlineCallbacks
def crawl():
    yield runner.crawl(mySpyder)
    reactor.stop()

crawl()
reactor.run()
#%%
