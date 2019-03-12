import time
import pytest
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from utils import constants as cs
import allure
import moment


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.launch_url(cs.URL)
        login.enter_un(cs.UN)
        login.enter_pwd(cs.PWD)
        login.click_login_btn()
        # driver.find_element_by_id("username").send_keys("admin")
        # driver.find_element_by_name("pwd").send_keys("manager")
        # driver.find_element_by_id("loginButton").click()
        time.sleep(5)

    def test_logout(self):
        try:
            driver = self.driver
            # driver.find_element_by_class_name("logout").click()
            home = HomePage(driver)
            home.clik_on_logout_link()
            x = driver.title
            assert x == "actiTIME - Login"
        except AssertionError as error:
            print(error)
            cur_time=moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            test_name=cs.whoami()
            screenshot_name=test_name+"_"+cur_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/Harish/PycharmProjects/Demo_Fr_1/screenshots/"+screenshot_name+".png")
            raise
        except:
            print("There is an error")
            raise
