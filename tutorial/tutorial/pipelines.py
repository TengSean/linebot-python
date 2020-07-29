# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from tutorial.richLogging import RL
from tutorial.pipelines_interface import Pipelines_Interface

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json


class TutorialPipeline:

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings['filename'])

    def __init__(self, filename):
        self.rl = RL()
        self.i = 0
        self.file_name = filename
        self._OUTPUT = {}



    def open_spider(self, spider):
        self.rl.info("Starting the spider pipeline...")
        self.rl.info(os.getcwd())
        self.file = open(f'{self.file_name}.json', 'w')
        # self.file.write('[\n')

    def close_spider(self, spider):
        self.rl.info("Closing the spider pipeline...")
        # self.file.write('\n]')
        line = json.dumps(self._OUTPUT, indent=4, ensure_ascii=False)
        self.file.write(line)
        self.file.close()




    def process_item(self, item, spider):

        # if 'json_handler' not in getattr(spider, 'pipelines', []):
        #     self.rl.info('Skip json_handler...')

        pipeline_interface = Pipelines_Interface()
        self._OUTPUT = pipeline_interface.Engine(item, spider)

        self.rl.debug(self._OUTPUT)

        
        self.rl.debug(self.i)
        
        return item
