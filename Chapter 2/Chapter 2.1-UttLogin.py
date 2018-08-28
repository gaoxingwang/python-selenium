# coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://192.168.1.1")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("pwd").send_keys("admin")
driver.find_element_by_id("login_btn").click()
#driver.quit()