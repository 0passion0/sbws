import asyncio
import os
import re
import time
import multiprocessing

import aiohttp
from selenium.webdriver import Firefox
async def fetch(session, url):
    print("发送请求:", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.read()
        file_name = os.path.join("E://图片", url.split('/')[-1])  # Update the file path to E://图片 folder
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)

async def imgs(url_list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in url_list:
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)
        await asyncio.wait(tasks)

def tlg(driver, page):
    url = f"https://wall.alphacoders.com/by_sub_category.php?id=167147&name=Dragon+Wallpapers&filter=4K+Ultra+HD&page={page}"
    driver.get(url)
    req = driver.page_source
    pattern = r'<meta itemprop="contentUrl" content="(https://[^"]+)">'
    image_urls = re.findall(pattern, req)

    print(f"Page {page} Image URLs:")
    img=[]
    for i in image_urls:
        img.append(i)
    print(img)
    asyncio.run(imgs(img))
def scrape_page(page):
    driver = Chrome()
    print(f"Scraping page {page}")
    tlg(driver, page)
    driver.close()
    print(f"Finished scraping page {page}")

def Cvn(n):
    processes = []
    for i in range(1, n + 1):
        process = multiprocessing.Process(target=scrape_page, args=(i,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

if __name__ == '__main__':
    print("Starting the scraping process...")
    Cvn(5)
    print("All processes completed.")
