import asyncio
import aiohttp
import requests
import re
import requests
import lxml
from lxml import etree
import time
'''url='http://pic.sogou.com/?ref=www.hifast.cn'
u=requests.get(url)
u.encoding='UTF-8'
print(u.text)'''
u=[]
async def aiodownload(u):
    name=u.rsplit("/")[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(u) as rep:
            with open(f'G:\\爬虫图片联系\\jojo.{name}.0.jpg',mode='wb') as f:
                f.write(await rep.content.read())#图片
                # rep.text()文本
                print('以完成第网址的爬取')

async def main():
    taske=[]
    for i in u:
        taske.append(aiodownload(i))
    await asyncio.wait(taske)
if __name__ == '__main__':
    name = input('请输入需要查询的图片名称（英文）:')
    kk= f"https://unsplash.com/s/photos/{name}"
    r = requests.get(kk)
    r.encoding = 'utf-8'
    r = r.text
    oj = re.compile(r'title="Download photo" href="(?P<nam>.*?)"><span ', re.S)
    r = oj.finditer(r)
    l = 1
    for i in r:
        a = i.group('nam')
        a = a.replace('?ixid=MnwxMjA3fDB8MXxzZWFyY2h8MTB8fGNhdHxlbnwwfHx8fDE2NTc1OTE3NzY&amp', '')
        u.append(a)
        l += 1
        print(f'第{l - 1}完成')
        time.sleep(1)
    print(u)
    print('网站地址提取完成')
    print('正在保存图片~~~~~~~')
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())