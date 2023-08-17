import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/67.0.3396.79 Safari/537.36'
}


def pic_scratch(url):
    res = requests.get(url, headers)
    links = re.findall('<a href=\"(.*)\" download>', res.text)
    for link in links:
        pic = requests.get(link, headers)
        pic_name = re.search('(?<=dl=).*\.jpg', link).group()
        with open('G:\\爬虫图片联系' + pic_name, 'wb') as pf:
            pf.write(pic.content)
        print("完成图片下载:" + pic_name)


if __name__ == '__main__':
    start_time = time.time()
    urls = ['https://www.pexels.com/search/dog/?page=={}'.format(i) for i in range(1, 7)]
    for url in urls:
        pic_scratch(url)
    end_time = time.time()
    print("总用时:", end_time - start_time)

