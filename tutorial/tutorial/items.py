# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BaseItem(scrapy.Item):

    ITEM_NAME = scrapy.Field()

    CRAWL_DATE = scrapy.Field()

    DATA_ATTRIBUTION = scrapy.Field()




class TutorialItem(BaseItem):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # pass
    CONTENT_TICKER = scrapy.Field()

    CONTENT_COMPANY = scrapy.Field()

    CONTENT_IDENTITY = scrapy.Field()

    CONTENT_NAME = scrapy.Field()

    CONTENT_TRANSACTION_DATE = scrapy.Field()

    CONTENT_MORTGAGE = scrapy.Field()

    CONTENT_REDEMPTION = scrapy.Field()

    CONTENT_CUMULATIVE_STOCK = scrapy.Field()

    CONTENT_PLEDGEE = scrapy.Field()

    CONTENT_MEMO = scrapy.Field()

    CONTENT_DECLARATION_DATE = scrapy.Field()

