# %%

from subprocess import Popen, PIPE
from datetime import datetime

file_name = str(datetime.today().strftime("%Y-%m-%d"))
p1 = Popen(['scrapy', 'crawl', 'stock_price'],
            cwd = './tutorial',
            stdout=PIPE)
p2 = Popen(["scrapy", "crawl", "spyder1",
            "-s", f"filename={file_name}"],
            cwd = './tutorial',
            stdout=PIPE)
out1,err1 = p1.communicate()
out2, err2 = p2.communicate()
# print(err)
print(out1.decode('utf-8'))
print(out2.decode('utf-8'))
# print(out)
# %%
# import datetime

# print(datetime.datetime.today().strftime("%Y-%m-%d"))

# %%


# a = {'BASIC_COMPANY': '台積電',
#     'CONTENT_CUMULATIVE_STOCK': '1,300,000',
#     'CONTENT_DECLARATION_DATE': '107/06/11',
#     'CONTENT_IDENTITY': '副總經理本人',
#     'CONTENT_MEMO': '\xa0',
#     'CONTENT_MORTGAGE': '0',
#     'CONTENT_NAME': '何麗梅',
#     'CONTENT_PLEDGEE': '兆豐國際商業銀行(股)公司竹科新安分公司',
#     'CONTENT_REDEMPTION': '200,000',
#     'BASIC_TICKER': '2330',
#     'CONTENT_TRANSACTION_DATE': '107/06/08'}
# for k, v in a.items():
#     if 'BASIC' in k:
#         print(k.split('_')[-1], v)

# %%
