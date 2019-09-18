from selenium import webdriver
from getpass import getpass

snu_id = input("ID:")
pwd = getpass("PASSWORD:")
driver = webdriver.Chrome('/home/thoum/chromedriver')
driver.implicitly_wait(3)
driver.get("https://etl.snu.ac.kr")
driver.find_element_by_id("input-username").send_keys(snu_id)
driver.find_element_by_id("input-password").send_keys(pwd)
driver.find_element_by_name("loginbutton").click()
