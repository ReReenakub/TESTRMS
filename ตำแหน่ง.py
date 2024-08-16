import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://bms.rmsoperation.com/")
time.sleep(10)
element = driver.find_element(By.ID, "username")
element.send_keys('rpchat11@mailoper.com')
time.sleep(0.5)
element2 = driver.find_element(By.ID, "password")
element2.send_keys('admin@123')
driver.find_element(By.XPATH, '//*[@id="login_area"]/div/div/div/div/form/div[3]/button').click()