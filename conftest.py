import pytest
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="browser firefox,chrome")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome(
            executable_path="C:/Users/Harish/PycharmProjects/Demo_Fr_1/drivers/chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(
            executable_path="C:/Users/Harish/PycharmProjects/Demo_Fr_1/drivers/geckodriver.exe")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.quit()
