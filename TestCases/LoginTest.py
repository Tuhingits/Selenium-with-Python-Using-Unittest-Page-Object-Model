import time
from selenium import webdriver
import unittest
import HtmlTestRunner
import sys
from PageObject import XLUtils

sys.path.append("C://Users/Tuhin/PycharmProjects/Selenium_Project_Using_POM")
from PageObject.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    Base_Url = "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.Base_Url)
        cls.driver.maximize_window()

    def testLogin(self):
        path = "C:/Users/Tuhin/Desktop/Automation/LoginCredentials.xlsx"
        rows = XLUtils.GetRow(path, 'Sheet1')
        for r in range(2, rows + 1):
            self.username = XLUtils.ReadData(path, "Sheet1", r, 1)
            self.password = XLUtils.ReadData(path, "Sheet1", r, 2)
            lp = LoginPage(self.driver)
            lp.Set_UserName(self.username)
            lp.Set_Password(self.password)
            lp.Click_login()
            Actual_URL = self.driver.current_url
            Expect_URL = "https://katalon-demo-cura.herokuapp.com/#appointment"
            if Actual_URL == Expect_URL:
                print("Login Test Pass")
                time.sleep(3)
                lp.Click_Menu()
                lp.Click_Logout()
                time.sleep(3)
            else:
                print("Login Test Fail")

            time.sleep(3)
            lp.Click_Menu()
            lp.Click_SideLogin()
            time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Report)'))
