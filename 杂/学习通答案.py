import time
from pynput import mouse,keyboard
import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import csv
u="http://127.0.0.1/"
res=requests.get(u)
res.encoding='utf-8'
html=etree.HTML(res.text)
tab=html.xpath("/html/body/div[3]/div[1]/div[2]/form/div/div")
#/html/body/div[3]/div[1]/div[2]/form/div/div[1]/h3
k=[]
ll=85
p=1
for i in tab:
        l=(i.xpath('./h3/text()'))
        '''a=i.xpath('./form/div/div[1]/div/text()')
        b = i.xpath('./form/div/div[2]/div/text()')
        c = i.xpath('./form/div/div[3]/div/text()')
        d = i.xpath('./form/div/div[4]/div/text()')'''
        kim=l
        print(kim)
        k.append(kim)
        p+=1
        ll-=1
time.sleep(6)
m_mouse=mouse.Controller()
m_keyboard=keyboard.Controller()
#m.mouse.posituon=(850,670)
m_mouse.click(mouse.Button.left)
for i in k:
    i=''.join(i)
    m_keyboard.type(f'{i}')
    m_keyboard.press(keyboard.Key.enter)
    m_keyboard.release(keyboard.Key.enter)
    time.sleep(2)