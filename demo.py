import time
from selenium import webdriver
driver = webdriver.Chrome("C:\\Users\\hp\\Desktop\\Selenium\\chromedriver.exe")

driver.set_page_load_timeout(10)

driver.get("https://www.google.com")

driver.find_element_by_name("q").send_keys("Abhi032 github")
driver.find_element_by_class_name("gNO89b").click()

time.sleep(5)
driver.close()
driver.quit()