class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.un_txt_bx_id = "username"
        self.pwd_txt_bx_id = "pwd"
        self.login_btn_id = "loginButton"

    def launch_url(self, url):
        self.driver.get(url)

    def enter_un(self, un):
        self.driver.find_element_by_id(self.un_txt_bx_id).send_keys(un)

    def enter_pwd(self, pwd):
        self.driver.find_element_by_name(self.pwd_txt_bx_id).send_keys(pwd)

    def click_login_btn(self):
        self.driver.find_element_by_id(self.login_btn_id).click()
