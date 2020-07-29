import scrapy
from scrapy_splash import SplashRequest, SplashFormRequest

from tutorial.items import TutorialItem
from tutorial.richLogging import RL

import os, time


class mySpyder(scrapy.Spider):
    name = 'spyder1'
    rl = RL()
    pipelines = ['return_json_handler']

    def start_requests(self, ):
        urls = [
            'https://mops.twse.com.tw/mops/web/STAMAK03_1',
        ]
        # self.rl.info(f'First arg is: {self.arg1}')
        lua = '''
        function main(splash, args)
            assert(splash:go(splash.args.url))
            assert(splash:wait(0.1))

            splash:select("input[id='co_id']"):send_text("2330")
            splash:select("input[id='b_date']"):send_text("1060701")
            splash:select("input[id='e_date']"):send_text("1090630")
            splash:select("input[value=' 查詢 ']"):mouse_click()
            splash:wait(3)

            return {html=splash:html()}
        end
        '''

        for url in urls:
            yield SplashRequest(url, 
                                self.parse,
                                endpoint = 'execute',
                                args = {
                                    'lua_source': lua
                                    }
                                )
        
    def parse(self, response):
        self.log('start parsing response')
        # self.log(response.text)
        for table in response.selector.xpath('//table[@class="hasBorder"]'):
            selector_list = table.xpath('//tr[@class="odd"]/td/text()|//tr[@class="even"]/td/text()')
            for i in range(0,len(selector_list), 12):

                item = TutorialItem()
                item['BASIC_TICKER'] = str(selector_list[i].get().strip(' '))
                item['BASIC_COMPANY'] = str(selector_list[i+1].get().strip(' '))
                item['CONTENT_IDENTITY'] = str(selector_list[i+3].get().strip(' '))
                item['CONTENT_NAME'] = str(selector_list[i+4].get().strip(' '))
                item['CONTENT_TRANSACTION_DATE'] = str(selector_list[i + 5].get().strip(' '))
                item['CONTENT_MORTGAGE'] = str(selector_list[i + 6].get().strip(' '))
                item['CONTENT_REDEMPTION'] = str(selector_list[i + 7].get().strip(' '))
                item['CONTENT_CUMULATIVE_STOCK'] = str(selector_list[i + 8].get().strip(' '))
                item['CONTENT_PLEDGEE'] = str(selector_list[i + 9].get().strip(' '))
                item['CONTENT_MEMO'] = str(selector_list[i + 10].get())
                item['CONTENT_DECLARATION_DATE'] = selector_list[i + 11].get()

                # self.rl.debug(f"ticker: {item['CONTENT_TICKER']}, company: {item['CONTENT_COMPANY']}, identity: {item['CONTENT_IDENTITY']}, name: {item['CONTENT_NAME']}, transaction_date: \
                #     {item['CONTENT_TRANSACTION_DATE']}, mortgage: {item['CONTENT_MORTGAGE']}, redemption: {item['CONTENT_REDEMPTION']}, cumulative_stock: {item['CONTENT_CUMULATIVE_STOCK']}, \
                #      pledgee: {item['CONTENT_PLEDGEE']}, memo: {item['CONTENT_MEMO']}, delcaration_date: {item['CONTENT_DECLARATION_DATE']}")

                # self.rl.debug(item)
                self.rl.info(f"Round {int(i/12+1)} Finish!")
                
                yield item
        