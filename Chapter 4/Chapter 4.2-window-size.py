from selenium import webdriver
driver = webdriver.Firefox()
#driver.get("http://m.mail.10086.cn")
driver.get("http://www.baidu.com")

#参数数字为像素点
#设置浏览器宽480，高800显示
#driver.set_window_size(480,800)

#设置浏览器全屏显示
driver.maximize_window()
#driver.quit()