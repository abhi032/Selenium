import time
from selenium import  webdriver
driver = webdriver.Chrome("C:\\Users\\hp\\Desktop\\Selenium\\chromedriver.exe")
driver.set_page_load_timeout(10)

driver.get("https://www.youtube.com/")
driver.find_element_by_name("search_query").send_keys(input())
driver.find_element_by_id("search-icon-legacy").click()
time.sleep(10)
driver.find_element_by_class_name("style-scope ytd-video-renderer").click()
time.sleep(300)
driver.close()
driver.quit()