from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://learn.letskodeit.com/")


element = driver.find_element(By.LINK_TEXT, 'Login').click()

driver.implicitly_wait(10)
driver.find_element(By.ID, 'user_email').send_keys('test')
driver.find_element(By.ID, 'user_passwordff').send_keys('test')
driver.find_element(By.NAME, 'commit').is_enabled()


