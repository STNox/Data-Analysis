import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome('C:\\Users\\shoseo\\Documents\\ChromeDriver\\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.opinet.co.kr/user/main/mainView.do')
time.sleep(1)

driver.find_element_by_css_selector('.ic_m1').click()
time.sleep(2)

region = driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]') # xpath 복사, 붙여넣기
# region = driver.find_element_by_id('SIGUNGU_NM0')
gu_list = region.find_elements_by_tag_name('option')

gu_names = [gu.get_attribute('value') for gu in gu_list]
""" gu_names = []
for gu in gu_list:
    gu.get_attribute('value')
    gu_names.append(name) """
del gu_names[0]

''' region = driver.find_element_by_id("SIGUNGU_NM0")
region.send_keys(gu_names[0])
time.sleep(1)

driver.find_element_by_xpath('//*[@id="glopopd_excel"]/span').click() '''

# 25개 자치구에 대해서 엑셀 다운로드
for gu in gu_names:
    region = driver.find_element_by_id("SIGUNGU_NM0")
    region.send_keys(gu)
    time.sleep(1)
    
    driver.find_element_by_xpath('//*[@id="glopopd_excel"]/span').click()
    time.sleep(2)