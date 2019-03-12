from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://azure.microsoft.com/en-in/")
driver.maximize_window()
driver.implicitly_wait(30)

# case 1
# driver.execute_script("window.scrollBy(0,1000)", "")

# case 2
# ele = driver.find_element_by_xpath("//*[text()='Artificial intelligence']")
# driver.execute_script("arguments[0].scrollIntoView();", ele)

# Case 3
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")