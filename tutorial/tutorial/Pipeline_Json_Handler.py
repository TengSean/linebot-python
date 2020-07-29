import json, os
from itemadapter import ItemAdapter

from tutorial.richLogging import RL

STRING_INIT = 'NA'
LIST_INIT = [ ]
DICT_INIT = {}

class Json_Handler:
    def __init__(self, ):
        self.rl = RL()

        self._SAVE_BASIC_LOCK = False
        self._SAVE_TEMPLATE = {
            'TICKER': STRING_INIT,
            'COMPANY': STRING_INIT,
            'CONTENT': LIST_INIT
        }
        self._CONTENT = DICT_INIT

    # * >> Start here <<
    def Engine(self, item):
        save_dict = ItemAdapter(item).asdict()
        self._Engine(save_dict)

    def _Engine(self, save_dict: dict):

        if (not self._SAVE_BASIC_LOCK):
            self._Save_basic_information(save_dict)
            self._SAVE_BASIC_LOCK = True

        self._Save_content_information(save_dict)

    def Output(self, ):
        return self._SAVE_TEMPLATE


    def _Save_basic_information(self, item: dict):

        self.rl.info('Saving Basic information')
        for k, v in item.items():
            if 'BASIC' in k:
                New_k = k.split('BASIC_')[-1]
                self._SAVE_TEMPLATE[New_k] = item[k]

    def _Save_content_information(self, item: dict):

        self.rl.info('Saving Content information')
        for k, v in item.items():
            if 'CONTENT' in k:
                New_k = k.split('CONTENT_')[-1]
                self._CONTENT[New_k] = item[k]
        self._SAVE_TEMPLATE['CONTENT'].append(self._CONTENT)