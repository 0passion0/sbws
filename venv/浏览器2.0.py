from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

web = Chrome()
web.get('https://alphacoders.com/')

# Find the search input field, input the value, and click the search button
search_input = web.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div/div[1]/form/div/input')
search_input.send_keys('鬼灭之刃')
time.sleep(3)

search_button = web.find_element(By.XPATH, '//*[@id="search_zone_index"]/span/button/i')
search_button.click()
time.sleep(3)

# Get the current URL after clicking the search button
current_url = web.current_url
print("Current URL:", current_url)

# Close the browser window
web.quit()

# web.find_element(By.XPATH,'//*[@id="first74130"]').click()
'''web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[4]/form/div/span/input').send_keys('lion',Keys.ENTER)
time.sleep(5)
web.find_element(By.XPATH,'//*[@id="loginBtn"]').click()
time.sleep(5)
web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[4]/span').click()
time.sleep(5)
web.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div[4]/div/a[2]').click()
time.sleep(3)
web.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]').click()
web.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[2]/div[1]/div/form/div/div[2]/input').click()'''

'''web.switch_to.window(web.window_handles[-1])
a=web.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[4]/div[1]/dl[1]/dd[2]/div/br[1]').text
print(a)'''