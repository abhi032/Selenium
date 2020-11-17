from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.fb.com")
print(driver.title)

driver.close()
driver.quit()
print("done")