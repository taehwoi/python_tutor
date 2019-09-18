from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
import time

userid = input("ID:")
pwd = getpass("PASSWORD:")
driver = webdriver.Chrome('/home/thoum/chromedriver')
driver.implicitly_wait(3)
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
driver.find_element_by_name("username").send_keys(userid)
driver.find_element_by_name("password").send_keys(pwd)

#might have to sleep here if slow

#find it by inspection mode
path_of_loginbtn = "//*[@id=\"react-root\"]/section/main/div\
                    /article/div/div[1]/div/form/div[4]/button/div"
driver.find_element_by_xpath(path_of_loginbtn).submit()
