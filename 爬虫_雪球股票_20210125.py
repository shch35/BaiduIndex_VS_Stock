import json
from urllib import request

# 因为不能访问  所以要加个头
headers = {
    #GET /interview/list/latest.json?count=5 HTTP/1.1,
    #Host: xueqiu.com,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
    #Accept: */*,
    #Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2,
    #Accept-Encoding: gzip, deflate, br,
    #Referer: https://xueqiu.com/S/sz000725,
    #X-Requested-With: XMLHttpRequest,
    #elastic-apm-traceparent: 00-292874f83b8dee2313bfa41d9f57ccb2-8c63173c1037ecd1-00,
    #Connection: keep-alive,
    'Cookie': '复制你的Cookie',
    }

# urllib 的 操作
url = 'https://stock.xueqiu.com/v5/stock/chart/kline.json?symbol=SZ000725&begin=979228800000&end=1611126596243&period=day&type=before&indicator=kline'
print(url)
# request.Request
req = request.Request(url, headers = headers)

# 通过request 请求 雪球网
response = request.urlopen(req)
#print(response)

res = response.read()      # 将内容获取出来
#print(res)
# 字符串, 需要转成dict/list      获取出来之后把转化成字符串


# 转换函数 res_dict = json.loads(res)
res_dict = json.loads(res)        #json 这个包  能够将一个字符串转换成python里的一个对象   它可以是dict/list
# 打印 res_dict
#print(res_dict)

list_json = res_dict['data']       # 然后获取dict里的list   然后遍历获取每一个值
#print(list_json)


list_symbol = list_json['symbol']
#print(list_symbol)

list_column = list_json['column']
#print(list_column)

list_item =list_json['item']
#print(list_item)


# import codecs
# import csv
#
# f = codecs.open('test.csv', 'w', 'utf_8_sig')  # 解决写入csv时中文乱码
# writer = csv.writer(f);
# for item in list_json:
#     writer.writerow([item['timestamp'], item['volume'], item['close']])
# f.close()
print('========================================================================')


# data_dumps = json.dumps(list_json, sort_keys=True, indent=4, separators=(',', ':'))
# #print(data_dumps)
#
# data_loads = json.loads(data_dumps)
# print(data_loads)


import csv

headers = list_column

print(headers)

values = list_item

print(values)


with open('test.csv','w',newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(headers)
    writer.writerows(values)
    
    
import pandas as pd

data_column_frame = pd.DataFrame(list_column)
print(data_column_frame)



data_item_frame = pd.DataFrame(list_item)
print(data_item_frame)

# data_item_frame.to_csv('baidu_gupiao_save.csv）
