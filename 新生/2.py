import asyncio
import re
import requests
from selenium import webdriver

pl = ['jpg', 'png', 'jpeg']
lianjie = []


async def get_image_links(page_num):
    driver = webdriver.Chrome()
    driver.get(f"https://wall.alphacoders.com/by_sub_category.php?id=312214&name=Jujutsu+Kaisen+Wallpapers&filter=4K+Ultra+HD&page={page_num}")
    req = driver.page_source
    oj = re.compile(r'<img class="img-responsive big-thumb thumb-desktop" .*? src="(?P<nam>.*?)"', re.S)
    r = oj.finditer(req)
    for i in r:
        a = i.group('nam')
        if a.split('.')[-1] in pl:
            lianjie.append(a)

    driver.close()


async def download_image(url):
    name = url.split('/')
    print(name[4])
    with open(f'e:\\图片\\{name[4]}', mode='wb+') as f:
        f.write(requests.get(url).content)


async def main():
    n = int(input("请输入页数："))
    tasks = []
    for i in range(n):
        tasks.append(get_image_links(i + 1))

    await asyncio.gather(*tasks)

    download_tasks = []
    for url in lianjie:
        download_tasks.append(download_image(url))

    await asyncio.gather(*download_tasks)


if __name__ == '__main__':
    asyncio.run(main())
