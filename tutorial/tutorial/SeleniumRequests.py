from scrapy import Request

class SeleniumRequest(Request):
    '''
    另外包裝的 Request 類別，用來判斷是否要使用 Selenium
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)