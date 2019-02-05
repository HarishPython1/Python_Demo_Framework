import time


class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.logout_link_id="logoutLink"

    def clik_on_logout_link(self):
        time.sleep(5)
        self.driver.find_element_by_id(self.logout_link_id).click()