import time

from selenium import webdriver

print("selenium Test Started")
driver = webdriver.Chrome(executable_path="C:/Users/Harish/PycharmProjects/Demo_Fr_1/drivers/chromedriver.exe")
driver.get("file:///C:/Users/Harish/Desktop/Login.html")
driver.find_element_by_id("emailid").send_keys("admin")
time.sleep(5)
driver.find_element_by_id("qspid").send_keys("manager")
time.sleep(5)
driver.find_element_by_id("btnid").click()
time.sleep(5)
driver.quit()
print("selenium Test Ended")