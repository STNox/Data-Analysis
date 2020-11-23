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

region = driver.find_element_by_xpath('//*[@id="SIGUNGU_NM0"]') # xpath 복사, 붙여넣기
# region = driver.find_element_by_id('SIGUNGU_NM0')
