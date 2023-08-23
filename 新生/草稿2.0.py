import time
from pynput import mouse,keyboard
import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import csv
u="https://dami8.me/vodtype/20.html"
res=requests.get(u)
res.encoding='utf-8'
# print(res.text)
s=f'title="(.*?)"'
d=re.findall(s,res.text)
print(d)