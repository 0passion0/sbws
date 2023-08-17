import re
import requests
import lxml
from lxml import etree
import time
u='http://192.168.5.30/tlg.html'
r = requests.get(u)
r.encoding = 'utf-8'
r=r.text
print(r)
oj=re.compile(r'ng-bind-html="file.statusHTML" class="ng-binding"><a class="download" href="(?P<nam>.*?)" target="_blank">',re.S)
r=oj.finditer(r)
l=1
for i in r:
        print(i)
        '''with open(f'G:\\爬虫图片联系\\{name}.{l}.0.jpg', mode='wb+') as f:
                f.write((requests.get(a).content))
        l+=1
        print(f'第{l-1}完成')
        time.sleep(1)'''
print('ok')



