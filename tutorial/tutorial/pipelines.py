# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from tutorial.richLogging import RL
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TutorialPipeline:
    def __init__(self, ):
        self.rl = RL()

    def open_spider(self, spider):
        self.rl.info(os.getcwd())
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.rl.info('This is process_item function')
        



        return item