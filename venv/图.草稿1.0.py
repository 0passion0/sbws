from lxml import etree  # 导入Xpath
import requests
import os

if __name__ == '__main__':

    url = "https://pic.netbian.com/4kdongman/index.html"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}
    res = requests.get(url, headers=headers).text.encode("ISO-8859-1")  # 中文转码
    tree = etree.HTML(res)  # 实例化HTML
    pictict = tree.xpath('//div[@class="slist"]//li')  # 获取<li>的数据
    if not os.path.exists("./pictict"):  # 创建文件以便保存图片
        os.mkdir("./pictict")
    for list in pictict:
        html = 'https://pic.netbian.com' + list.xpath("./a/img/@src")[0]  # 循环获取图片的url
        name = list.xpath("./a/img/@alt")[0] + ".png"  # 获取图片名称
        pictict_get = requests.get(url=html, headers=headers).content  # 进行持久化存储
        name_path = "pictict/" + name  #

        with open(name_path, "wb") as f:
            f.write(pictict_get)
            print(name, "下载完成")

    page = input("页数：")  # 因为第一张和后面的不太一样所以就从新写了一个
    page = int(page)
    for i in range(page):
        url_next = "https://pic.netbian.com/4kdongman/index_{}.html".format(page)
        get_next = requests.get(url_next, headers=headers).text.encode("ISO-8859-1")
        tree_next = etree.HTML(get_next)
        pictict_next = tree_next.xpath('//div[@class="slist"]//li')
        for list2 in pictict_next:
            html_next = 'https://pic.netbian.com' + list2.xpath("./a/img/@src")[0]
            name_next = list2.xpath("./a/img/@alt")[0] + ".png"
            pictict_get_next = requests.get(url=html_next, headers=headers).content
            name_path_next = "pictict/" + name_next
            with open(name_path_next, "wb") as f:
                f.write(pictict_get_next)
                print(name_next, "下载完成")