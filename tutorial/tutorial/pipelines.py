# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
from tutorial.richLogging import RL
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import codecs, json

STRING_INIT = 'NA'
LIST_INIT = [ ]

class TutorialPipeline:

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings['filename'])

    def __init__(self, filename):
        self.rl = RL()
        self.i = 0
        self.file_name = filename
        self._SAVE_BASIC_LOCK = False
        self._SAVE_TEMPLATE = {
            'TICKER': STRING_INIT,
            'COMPANY': STRING_INIT,
            'CONTENT': LIST_INIT
        }
        self._CONTENT = {
            "IDENTITY": STRING_INIT,
            "NAME": STRING_INIT,
            "TRANSACTION_DATE": STRING_INIT,
            "MORTGAGE": STRING_INIT,
            "REDEMPTION": STRING_INIT,
            "CUMULATIVE_STOCK": STRING_INIT,
            "PLEDGEE": STRING_INIT,
            "MEMO": STRING_INIT,
            "DECLARATION_DATE": STRING_INIT
        }



    def open_spider(self, spider):
        self.rl.info("Starting the spider pipeline...")
        self.rl.info(os.getcwd())
        self.file = open(f'{self.file_name}.json', 'w')
        # self.file.write('[\n')

    def close_spider(self, spider):
        self.rl.info("Closing the spider pipeline...")
        # self.file.write('\n]')
        line = json.dumps(self._SAVE_TEMPLATE, indent=4, ensure_ascii=False)
        self.file.write(line)
        self.file.close()

    def _Save_Basic_Information(self, item: dict):
        self.rl.info('Saving Basic information')
        for k, v in item.items():
            if 'BASIC' in k:
                New_k = k.split('BASIC_')[-1]
                self._SAVE_TEMPLATE[New_k] = item[k]

    def _Save_Content_Information(self, item: dict):
        self.rl.info('Saving Content information')
        for k, v in item.items():
            if 'CONTENT' in k:
                New_k = k.split('CONTENT_')[-1]
                self._CONTENT[New_k] = item[k]
        self._SAVE_TEMPLATE['CONTENT'].append(self._CONTENT)

    def process_item(self, item, spider):
        self.i+=1
        self.rl.info('This is process_item function')
        self.rl.debug(self._SAVE_TEMPLATE)
        self.rl.debug(self._CONTENT)
        # self.rl.debug(ItemAdapter(item).asdict())
        Save_Dict = ItemAdapter(item).asdict()

        if( not self._SAVE_BASIC_LOCK):
            self._Save_Basic_Information(Save_Dict)
            self._SAVE_BASIC_LOCK = True
        self._Save_Content_Information(item)
        self.rl.debug(self._SAVE_TEMPLATE)
        
        self.rl.debug(self.i)
        return item
