import re
import requests
import lxml
from lxml import etree
import time
name=input('请输入需要查询的图片名称（英文）:')
u =f"https://unsplash.com/s/photos/{name}"
r = requests.get(u)
r.encoding = 'utf-8'
r=r.text
oj=re.compile(r'title="Download photo" href="(?P<nam>.*?)"><span ',re.S)
r=oj.finditer(r)
l=1
for i in r:
        a=i.group('nam')
        a = a.replace('?ixid=MnwxMjA3fDB8MXxzZWFyY2h8MTB8fGNhdHxlbnwwfHx8fDE2NTc1OTE3NzY&amp', '')
        print(a)
        with open(f'G:\\爬虫图片联系\\{name}.{l}.0.jpg', mode='wb+') as f:
                f.write((requests.get(a).content))
        l+=1
        print(f'第{l-1}完成')
        time.sleep(1)
print('ok')



