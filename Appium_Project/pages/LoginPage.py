from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class LoginPage(BasePage):
    elm_userName = (By.ID,"com.longfor.app.turbo.beta:id/mobile")    #用户名输入框
    elm_pwd = (By.ID,"com.longfor.app.turbo.beta:id/auth_code")    #密码输入框
    elm_loginBtn = (By.ID,"com.longfor.app.turbo.beta:id/login_by_auth_code")    #登录按钮
    elm_alert = (By.ID,"com.longfor.app.turbo.beta:id/tv_ok")

    def inputUserName(self,username):
        self.driver.find_element(*self.elm_userName).send_keys(username)

    def inputPwd(self,pwd):
        self.driver.find_element(*self.elm_pwd).send_keys(pwd)

    def clickLoginBtn(self):
        self.driver.find_element(*self.elm_loginBtn).click()

    def clickalert(self):
        print(1,*self.elm_alert)
        self.driver.find_element(*self.elm_alert).click()

if __name__=="__main__":
    pass
