from selenium import webdriver
co = webdriver.ChromeOptions()
co.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=co, executable_path= "C:\\Users\\hp\\Desktop\\Selenium\\chromedriver.exe")
driver.get("https://www.google.com")
print(driver.title)
driver.close()
driver.quit()
print("All Good")