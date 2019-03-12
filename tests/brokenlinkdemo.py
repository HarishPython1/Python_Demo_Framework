from selenium import webdriver
import requests

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()
driver.implicitly_wait(30)

elements = driver.find_elements_by_tag_name("a")
print(len(elements))

b1 = []
l1 = []

for i in elements:
    #print(i.get_attribute("href"))
    r = requests.head(i.get_attribute("href"))
    #print(r.status_code)

    if r.status_code != 200:
        b1.append(i.get_attribute("href"))
    else:
        l1.append(i.get_attribute("href"))

    # for b in b1:
    #     print("broken links ", b)
    #
    # for c in l1:
    #     print("correct links ", c)

print("broken links ", b1)
print("working links", l1)
