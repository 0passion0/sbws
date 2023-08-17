import time
from pynput import mouse,keyboard
import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import csv
u="https://www.pexels.com/zh-cn/"
header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }
res=requests.get(u)
res.encoding='utf-8'
html=etree.HTML(res.text)
tab=html.xpath("/html/body/div[2]/main/div[3]/div[1]/div/div[1]")
print(tab)
k=[]
ll=85
p=1
for i in tab:
        l=(i.xpath('./article/div/a/text()'))
        kim=l
        print(kim)
        k.append(kim)
print(k)
