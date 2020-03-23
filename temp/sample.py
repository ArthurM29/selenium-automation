from selenium import webdriver



# driver = webdriver.Firefox(executable_path="drivers/geckodriver_v0.26.0/geckodriver")
# driver = webdriver.Chrome(executable_path="drivers/chromedriver_v80.0.3987.106/chromedriver")
# driver = webdriver.Ie(executable_path="drivers/ie_driver_v_3.150.1/IEDriverServer.exe")
driver = webdriver.Safari()

driver.get("http://www.python.org")
assert "Python" in driver.title
driver.close()
