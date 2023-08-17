import time
from pynput import mouse,keyboard
import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import csv
u="http://192.168.5.30/tlg.html"
res=requests.get(u)
res.encoding='utf-8'
html=etree.HTML(res.text)
tab=html.xpath("/html/body/div[3]/div[2]")
a=[]
k=[]
for i in tab:
        k=(i.xpath('./div/div/div/h3/div/text()'))
        print(k)
'''time.sleep(6)
m_mouse=mouse.Controller()
m_keyboard=keyboard.Controller()
#m.mouse.posituon=(850,670)
m_mouse.click(mouse.Button.left)
for i in k:
    i=''.join(i)
    m_keyboard.type(f'{i}')
    m_keyboard.press(keyboard.Key.enter)
    m_keyboard.release(keyboard.Key.enter)
    time.sleep(6)'''
