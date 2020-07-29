from tutorial.richLogging import RL
from tutorial.Pipeline_Json_Handler import Json_Handler

class Pipelines_Interface(object):
    def __init__(self, ):
        self.rl = RL()
        self._OUTPUT = None
        self.handler = {
            'return_json_handler' : Json_Handler()
        }
    
    def Engine(self, item , spider):

        return self._Engine(item, spider)

    def _Engine(self, item, spider):
        for p in getattr(spider, 'pipelines', []):
            self.rl.debug(p)
            self.handler[p].Engine(item)
            if 'return_' in p:
                self._OUTPUT = self.handler[p].Output()

        return self._OUTPUT