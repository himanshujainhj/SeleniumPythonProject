from selenium.webdriver.common.by import By
from POMDemo.Locators.locators import Locators
class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = Locators.welcome_link_id
        # self.welcome_link_id = "welcome"
        self.logout_link_xpath = Locators.logout_link_xpath
        # self.logout_link_xpath = '//*[@id="welcome-menu"]/ul/li[3]/a'

    def click_welcome(self):
        self.driver.find_element("id", self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()

