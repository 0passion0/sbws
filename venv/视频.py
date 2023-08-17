import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
import urllib
import time
import image
url='https://www.pearvideo.com/video_1766868'
cont=url.split('_')[1]
sta=f'https://www.pearvideo.com/videoStatus.jsp?contId={cont}&mrd=0.954790938435043'
h={
    'Referer': url,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
}
sin=requests.get(sta,headers=h)
s=sin.json()
srl=s['videoInfo']['videos']['srcUrl']
sys=s['systemTime']
srl=srl.replace(sys,f'cont-{cont}')
with open("D:\\爬虫图片联系\\k5.mp3",mode='wb') as f:
    f.write(requests.get(srl).content)
