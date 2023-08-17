import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
import  time
if __name__ == '__main__':
   u = "https://music.163.com/#/search/m/?s=%E8%92%99%E5%8F%A4%E4%BC%B4%E5%A5%8F"
   header = {
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52"
        }
   r = requests.get(u,headers=header)
   r.encoding = 'utf-8'
   r = r.text
   oj = re.compile(r"<div class='boxgrid'>.*?src=(?P<nam>.*?) alt", re.S)
   r = oj.finditer(r)
   l = 1
   for i in r:
      a = i.group('nam')
      a = a.replace('"', '')
      nam = a.rsplit("/", 1)[1]
      print(nam)
      with open(f'G:\\死神2\\{l}+{nam}', mode='wb+') as f:
         f.write((requests.get(a).content))
      l += 1
      time.sleep(5)

