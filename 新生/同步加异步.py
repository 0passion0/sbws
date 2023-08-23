import concurrent.futures  # 导入并发处理库
import os  # 导入操作系统库
import re  # 导入正则表达式库
import time

import aiohttp  # 导入异步 HTTP 请求库
import asyncio  # 导入异步编程库
from selenium.webdriver import Firefox  # 从 Selenium 库导入 Chrome WebDriver

# 异步下载函数，使用 aiohttp 库
async def fetch(session, url):
    print("Sending request:", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.read()
        file_name = os.path.join("E://图片", url.split('/')[-1])  # 更新文件路径到 E://图片 文件夹
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)

# 异步下载多张图片的函数
async def imgs(url_list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in url_list:
            task = asyncio.create_task(fetch(session, url))  # 创建异步任务
            tasks.append(task)  # 将任务添加到任务列表
        await asyncio.wait(tasks)  # 等待所有任务完成

# 使用 Selenium 获取图片链接并下载的函数
def tlg(driver, page):
    # https://wall.alphacoders.com/tag/suguru-geto-wallpapers?page=2
    url = f"https://wall.alphacoders.com/by_sub_category.php?id=167147&name=Dragon+Wallpapers&filter=4K+Ultra+HD&page={page}"  # 构建页面 URL
    driver.get(url)  # 打开页面
    time.sleep(2)
    req = driver.page_source  # 获取页面源代码

    pattern = r'<meta itemprop="contentUrl" content="(https://[^"]+)">'  # 使用正则表达式匹配图片链接
    image_urls = re.findall(pattern, req)  # 在页面源代码中查找匹配的图片链接

    print(f"Page {page} Image URLs:")
    img = []
    for i in image_urls:
        img.append(i)  # 将图片链接添加到列表
    print(img)
    asyncio.run(imgs(img))  # 调用异步下载函数下载图片

# 页面爬取函数
def scrape_page(page):
    driver = Firefox()  # 创建 Chrome WebDriver 实例
    print(f"Scraping page {page}")
    tlg(driver, page)  # 调用 Selenium 获取链接并异步下载图片
    driver.close()  # 关闭 WebDriver 实例
    print(f"Finished scraping page {page}")

# 控制多个页面爬取的函数
def Cvn(total_pages, max_workers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 使用线程池进行并发处理
        futures = [executor.submit(scrape_page, page) for page in range(1, total_pages + 1)]

    for future in concurrent.futures.as_completed(futures):
        # 处理已完成的任务，这里暂时没有特别的处理
        pass

if __name__ == '__main__':
    print("Starting the scraping process...")
    Cvn(total_pages=5, max_workers=5)  # 根据需要调整要处理的总页面数和最大同时处理任务的数量
    print("All processes completed.")
