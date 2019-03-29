import requests
import re
from xlwt import Workbook
import xlrd
import time

def key_name( number ):
    #获取页面的内容并返回
    name = '手机'
    URL_1 = "https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20170905&stats_click=search_radio_all%3A1&js=1&imgfile=&q="
    URL_2 = "&suggest=0_1&_input_charset=utf-8&wq=u&suggest_query=u&source=suggest&p4ppushleft=5%2C48&s="
    URL = ( URL_1 + name + URL_2 + str(number))
    #print(URL)
    res = requests.get( URL )
    return res.text

def find_date( text):
    #根据整个页面的信息，获取商品的数据所在的HTML源码并放回
    reg = r',"data":{"spus":\[({.+?)\]}},"header":'
    reg = re.compile(reg)
    info = re.findall(reg, text)
    return info[0]

def manipulation_data( info, N, sheet ):
    #解析获取的HTML源码，获取数据
    Date = eval(info)

    for d in Date:
        T = " ".join([t['tag'] for t in d['tag_info']])
        #print(d['title'] + '\t' + d['price'] + '\t' + d['importantKey'][0:len(d['importantKey'])-1] + '\t' + T)
        
        sheet.write(N,0,d['title'])
        sheet.write(N,1,d['price'])
        sheet.write(N,2,T)
        N = N + 1
    return N
    
    
def main():
    
    book = Workbook()
    sheet = book.add_sheet('淘宝手机数据')
    sheet.write(0,0,'品牌')
    sheet.write(0,1,'价格')
    sheet.write(0,2,'配置')
    book.save('淘宝手机数据.xls')
    #k用于生成链接，每个链接的最后面的数字相差48.
    #N用于记录表格的数据行数，便于写入数据
    k = 0
    N = 1
    for i in range(10+1):
        text = key_name( k + i * 48 )
        info = find_date(text)
        N = manipulation_data( info ,N, sheet )
    
        book.save('淘宝手机数据.xls')
        print('下载第' + str(i) + '页完成')

if __name__ == '__main__':
    main()