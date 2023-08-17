import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import csv
f=open("data.csv", mode='w+', encoding='utf-8')
csvwriter=csv.writer(f)
def daw(u):
    res=requests.get(u)
    res.encoding='utf-8'
    html=etree.HTML(res.text)
    tab=html.xpath('/html/body/div/div/div/div[4]/div[3]/div[1]/div[3]/div/div')
    for i in tab:
        s=i.xpath('./div[1]/div[3]/a/text()')
        csvwriter.writerow(s)
        print('提取完')
if __name__ == '__main__':
    #daw('http://www.shucai123.com/price/t1')
    with ThreadPoolExecutor(101) as t:
        for i in range(1,100):
            t.submit(daw,f'https://task.epwk.com/page{i}.html?k=python')
            print('完成')