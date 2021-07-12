from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("thoughworks")
driver.find_element_by_id("su").click()
time.sleep(8)

driver.close()