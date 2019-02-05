import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:/Users/Harish/PycharmProjects/Demo_Fr_1/drivers/chromedriver.exe")
# driver.get("http://facebook.com")
driver.get("http://www.facebook.com")
# driver.get("facebook.com")  #error -Cannot navigate to invalid URL

driver.find_element_by_id("u_0_j").send_keys("Test")
driver.find_element_by_id("u_0_l").send_keys("Test1")
day = Select(driver.find_element_by_id("day"))
day.select_by_value("22")

#time.sleep(5)
month = Select(driver.find_element_by_id("month"))
month.select_by_value("3")

#time.sleep(5)
year = Select(driver.find_element_by_id("year"))
year.select_by_value("1995")

driver.quit()
