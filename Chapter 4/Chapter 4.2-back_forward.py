from selenium import webdriver
driver = webdriver.Firefox()

first_url = "http://www.baidu.com"
print("now  access to %s" %(first_url))
driver.get(first_url)

second_url = "http://news.baidu.com"
print("now  access to %s" %(second_url))
driver.get(second_url)

print("back to %s" %(first_url))
driver.back()

print("forward to %s" %(second_url))
driver.forward()