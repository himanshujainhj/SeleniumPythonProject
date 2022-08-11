import time
import unittest

# imports for command line
import sys
import os

import HtmlTestRunner

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from POMDemo.Pages.loginPage import LoginPage
from POMDemo.Pages.homePage import HomePage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        # driver.maximize_window()
        #
        # driver.find_element("id", "txtUsername").send_keys("Admin")
        #
        # driver.find_element("id", "txtPassword").send_keys("admin123")
        #
        # driver.find_element("id", "btnLogin").click()
        #
        # driver.find_element("id", "welcome").click()
        #
        # driver.find_element(By.XPATH, '//*[@id="welcome-menu"]/ul/li[3]/a').click()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Himanshu Jain/PycharmProjects/Selenium/reports"))
