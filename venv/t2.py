import asyncio
import aiohttp
import requests
from aiohttp import TCPConnector
import re
import requests
import lxml
from lxml import etree
import time
k=[]
ll=1
async def aiodownload(uk):
    #print(uu)
    if uk not in k:
        name = uk.rsplit("/", 1)[1]
        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
        }
        async with aiohttp.ClientSession(connector=TCPConnector(ssl=False)) as session:
            timeouts = aiohttp.ClientTimeout(total=15 * 60)
            async with session.get(uk, headers=header, timeout=timeouts) as rep:
                timew=time.time()
                with open(f'g:\\\爬虫图片联系\\{name}', mode='wb') as f:  # 改地址的地方
                    f.write(await rep.content.read())  # 图片
                    # rep.text()文本
                    print('已完成一张照片的爬取，完成时间为：',end='')
                    timem = time.time()
                    print(timem-timew)

    else:
        print("图片已存在")

async def main(uu):
    taske=[]
    for i in uu:
        taske.append(aiodownload(i))
    await asyncio.wait(taske)
if __name__ == '__main__':
    l=1
    for j in range(1,5):
        uu = []
        for i in range(j, j+1):
            u = f"https://wall.alphacoders.com/by_collection.php?id=128name=Pacific+Rim+Wallpapers&filter=4K+Ultra+HD&page={i}"
            r = requests.get(u)
            r.encoding = 'utf-8'
            r = r.text
            oj = re.compile(r"<div class='boxgrid'>.*?src=(?P<nam>.*?) alt", re.S)
            r = oj.finditer(r)
            for i in r:
                a = i.group('nam')
                a = a.replace('"', '')
                print(a)
                uu.append(a)
                l += 1
                print(f'第{l - 1}完成')
        #print(uu)
        print('网站地址提取完成')
        print('正在保存图片~~~~~~~')
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(uu))
        print(f'已完成第{j}页')
        ll+=1
        k.append(uu)
        #time.sleep(20)