import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import csv
f=open("data.csv",mode='w+',encoding='utf-8')
csvwriter=csv.writer(f)
def daw(u):
    res=requests.get(u)
    res.encoding='utf-8'
    html=etree.HTML(res.text)
    tab=html.xpath("/html/body/div[3]/table/tr")
    #/html/body/div[3]/table/tbody/tr[2]/td[4]/p[1]/text()
    l=1
    for i in tab:
        if l==1:
            l=0
            continue
        a=i.xpath('./td[4]/p[1]/text()[1]')
        b=i.xpath('./td[4]/p[1]/b/text()')
        c=i.xpath('./td[4]/p[1]/text()[2]')
        '''a=''.join(a)
        b=''.join(b)
        c=''.join(c)'''
        s=a+b+c
        csvwriter.writerow(s)
        print('提取完')
if __name__ == '__main__':
    #daw('http://www.shucai123.com/price/t1')
    with ThreadPoolExecutor(101) as t:
        for i in range(1,100):
            t.submit(daw,f'http://www.shucai123.com/price/t{i}')
            print('完成')