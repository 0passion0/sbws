import re
import requests
import lxml
from lxml import etree
from bs4 import BeautifulSoup
import urllib
import time
import image
u='https://www.douyin.com/user/MS4wLjABAAAA5YYjuxmfxUvm1EI7zqaWid2-CW9FfyAjwYKVcwmirNA'
header = {
    "Cookie": "ttcid=05434a0f00264120a111059d1665806a10; tt_scid=lQrOS8EcNA.qdynmyPRjF1SDQRCp58Wr9JdKuiBjmllMAUxPiZbEiiasL4Qjc1qBd1a9; msToken=Gc5ooZVU3bEG1bZfWjh2iAnlU_aK13KreYvN0roQPl08IEtTkBIBDZN8Ydxw3di4evs74t9ZFwdfJySiWnKHgUEraOhfKA-AEspoZ1FtX9E9MgkkB3Z3CxX4ymrR5_lX",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}
url=requests.get(u,headers=header)
url.encoding='utf-8'
oj=re.compile(r'<ul class="ARNw21RN">.*?<a href="//(?P<nam>.*?)"',re.S)
r=oj.finditer(url)
print(r)
'''l=1
for i in r:
        a=i.group('nam')
        with open(f'D:\\抖音\\{l}.0.jpg', mode='wb+') as f:
                f.write((requests.get(a).content))
        l+=1
        print(f'第{l-1}完成')
        time.sleep(1)
print('ok')'''