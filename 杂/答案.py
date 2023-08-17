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
r = res.text
k=[]
oj = re.compile(r'class="rendered-markdown"><p>(?P<nam>.*?)<', re.S)
r = oj.finditer(r)
l = 1
for i in r:
      a = i.group('nam')
      a=f'{l}'+a
      print(a)
      k.append(a)
      l+=1
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
    time.sleep(3)