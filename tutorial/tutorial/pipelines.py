# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import logging
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TutorialPipeline:

    def open_spider(self, spider):
        logging.log(logging.INFO, os.getcwd())
        self.file = open('items.jl', 'w')
    def close_spider(self, spider):
        self.file.close()
    def process_item(self, item, spider):
        return item