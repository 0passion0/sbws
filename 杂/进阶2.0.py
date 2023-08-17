import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup


u ="https://music.163.com/#/search/m/?s=%E8%92%99%E5%8F%A4%E4%BC%B4%E5%A5%8F"
h={
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
   # 'cookie': 'msToken=GDt1sjHpfz3Q8i8Tddp_JkC_C8YA6_Pk5jGntBcMp5pgmxphNMikRKHet_4KRkAMrPXJptUqOZ5tJDr41RhxA0EXl30zp3GqsbPN7deiVJwJJ9GV1EvHDPLznMAjdP7u0w=='
}
r = requests.get(u,headers=h)
r.encoding = 'utf-8'
html = etree.HTML(r.text)
print(html)
dai = html.xpath("/html/body/div[3]/div/div[2]/div[2]/div")
print(dai)
for i in dai:
   print( i.xpath('./a/text()'))