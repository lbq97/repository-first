import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
print(curPath)
print(rootPath)
import pytest
from util.LoggingUtil import LoggingUtil
from pages.BasePage import BasePage
# from pages.WelcomePage import WelcomePage
from pages.LoginPage import LoginPage
# from pages.MainPage import MainPage
import logging
from appium import webdriver
import time
import allure


@allure.feature('测试登录功能')
class Test_login(object):
    '''类注释
    详细描述
    Attributes:
        属性说明
    '''

    def setup_method(self, method):
        self.logging_util = LoggingUtil()
        self.logging_util.setup_logging()
        self.logger = logging.getLogger()
        desired_caps = {
            'platformName': 'Android',
            # 'deviceName': '127.0.0.1:5554',  # 手机设备名称，通过adb devices查看
            'deviceName': '127.0.0.1:5555',  # 手机设备名称，通过adb devices查看
            'platformVersion': '6.0.1',  # android系统的版本号
            'appPackage': 'com.longfor.app.turbo.beta',  # apk包名
            # apk的launcherActivity
            'appActivity': 'com.longfor.app.turbo.business.login.LoginByAuthCodeActivity',
        }
        self.logger.info('启动app')
        try:
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            time.sleep(3)
            self.base_page = BasePage(self.driver)
            # self.welcome_page = WelcomePage(self.base_page)
            self.login_page = LoginPage(self.base_page)
            # self.main_page = MainPage(self.base_page)
        except Exception:
            BasePage.get_screen(screenshot_path='../screen_shot/')

    def teardown_method(self, method):
        print("断开连接")

    @allure.story('登录-用户不存在')
    def test_login_1(self):
        self.logger.info('开始测试test_login_1==================================')
        # self.base_page.swipe_to_left()
        # self.base_page.swipe_to_left()
        # self.welcome_page.click_tiyan_button()
        # self.welcome_page.click_login_button()
        self.login_page.clickalert()
        self.login_page.inputUserName('15628811988')
        self.login_page.inputPwd('12345678')
        self.login_page.clickLoginBtn()
        res = self.base_page.is_toast_exist('未知的异常')
        assert res
        self.logger.info('测试结束=====================================')

if __name__=="__main__":
    pytest.main()