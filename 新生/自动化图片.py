import re
import time
import multiprocessing
import requests
from selenium import webdriver
from selenium.webdriver import Chrome
import os
from multiprocessing import Pool

# 下载图片的函数
def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"已下载 {url} 并保存为 {save_path}")
    else:
        print(f"无法下载 {url}")

# 使用Selenium获取图片链接的函数
def tlg(driver, page):
    url = f"https://wall.alphacoders.com/by_sub_category.php?id=312213&name=Demon+Slayer%3A+Kimetsu+no+Yaiba+Wallpapers&filter=4K+Ultra+HD&page={page}"
    driver.get(url)
    time.sleep(5)
    req = driver.page_source
    pattern = r'<meta itemprop="contentUrl" content="(https://[^"]+)">'
    image_urls = re.findall(pattern, req)

    print(f"Page {page} Image URLs:")
    img = []
    for i in image_urls:
        img.append(i)
    print(img)
    save_folder = "E://图片"  # 图片保存路径
    os.makedirs(save_folder, exist_ok=True)

    processes = 3  # 并行进程的数量

    # 创建进程池
    with Pool(processes) as pool:
        for idx, url in enumerate(img):
            # filename = f"image_{idx + 1}.jpg"
            print(url.split('/')[-1])
            save_path = os.path.join(save_folder, url.split('/')[-1])
            # 使用apply_async方法提交下载任务给不同的进程
            pool.apply_async(download_image, args=(url, save_path))

        pool.close()  # 关闭进程池
        pool.join()  # 等待所有进程完成

    print("所有下载已完成。")

# 爬取页面内容的函数
def scrape_page(page):
    driver = Chrome()  # 创建一个Chrome浏览器实例
    print(f"Scraping page {page}")
    tlg(driver, page)  # 调用获取图片链接函数
    driver.close()  # 关闭浏览器实例
    print(f"Finished scraping page {page}")
    time.sleep(2)  # 等待2秒

# 启动多进程爬取函数
def Cvn(n):
    processes = []
    for i in range(1, n + 1):
        process = multiprocessing.Process(target=scrape_page, args=(i,))
        processes.append(process)
        process.start()  # 启动进程
    for process in processes:
        process.join()  # 等待所有进程完成

if __name__ == '__main__':
    print("Starting the scraping process...")
    Cvn(5)  # 启动多进程爬取5页内容
    print("All processes completed.")
