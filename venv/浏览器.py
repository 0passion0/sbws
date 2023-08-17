from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
web=Firefox()
web.get('https://www.12306.cn/index/')
print(web.page_source)
# time.sleep(1)
# a=web.find_element(By.XPATH,'//*[@id="J-btn-login"]')
# a.click()
# time.sleep(1)
# web.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys('13294759221')
# web.find_element(By.XPATH,'//*[@id="J-password"]').send_keys('Btlg2002')
# time.sleep(3)
# web.find_element(By.XPATH,'//*[@id="J-login"]').click()



'''li=web.find_elements(by=By.XPATH,value='/html/body/div/div/div/div[4]/div[3]/div[1]/div[3]/div/div')
for l in li:
    print(l.find_element(By.XPATH,'./div[1]/div[3]/a').text)'''
