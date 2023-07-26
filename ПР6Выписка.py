import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('D:/Tools/chromedriver.exe')
driver = selenium.webdriver.Chrome(service=s)
driver.get('https://idemo.bspb.ru')
driver.maximize_window()
driver.find_element(By.XPATH, "//*[@id='login-form']/div[1]/input").clear()
driver.find_element(By.XPATH, "//*[@id='login-form']/div[1]/input").send_keys("demo")
driver.find_element(By.XPATH, "//*[@id='login-form']/div[2]/input").clear()
driver.find_element(By.XPATH, "//*[@id='login-form']/div[2]/input").send_keys("demo")
driver.find_element(By.XPATH, "//*[@id='login-button']").click()
driver.find_element(By.XPATH, "//*[@id='otp-code']").clear()
driver.find_element(By.XPATH, "//*[@id='otp-code']").send_keys("0000")
driver.find_element(By.XPATH, "//*[@id='login-otp-button']").click()
driver.get("https://idemo.bspb.ru/statement")
driver.find_element(By.XPATH, "//*[@id='single-account']/div/select/option[13]").click()
driver.find_element(By.XPATH, "//*[@id='from-date']/input").clear()
driver.find_element(By.XPATH, "//*[@id='from-date']/input").send_keys("10.03.2023")
driver.find_element(By.XPATH, "//*[@id='until-date']/input").clear()
driver.find_element(By.XPATH, "//*[@id='until-date']/input").send_keys("27.06.2023")
driver.find_element(By.XPATH, "//*[@id='query-button']").click()
