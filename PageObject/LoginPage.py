from selenium.webdriver.common.by import By
from selenium import webdriver


class LoginPage():
    TextBox_name = "txt-username"
    TextBox_Password = "txt-password"
    Button_name = "/html/body/section/div/div/div[2]/form/div[4]/div/button"

    def __init__(self, driver):
        self.driver = driver

    def Set_UserName(self, username):
        self.driver.find_element(By.ID, self.TextBox_name).send_keys(username)

    def Set_Password(self, password):
        self.driver.find_element(By.ID, self.TextBox_Password).send_keys(password)

    def Click_login(self):
        self.driver.find_element(By.XPATH, self.Button_name).click()

    def Click_Menu(self):
        self.driver.find_element(By.ID, "menu-toggle").click()

    def Click_SideLogin(self):
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()

    def Click_Logout(self):
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()


