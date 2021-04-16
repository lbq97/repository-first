from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
import time
from util.LoggingUtil import LoggingUtil
import logging
import datetime

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
        LoggingUtil.setup_logging(LoggingUtil)
        self.logger = logging.getLogger()

    def find_element(self,*loc):
        try:
            # print(2,*loc)     *loc=id com.longfor.app.turbo.beta.debug:id/tv_ok
            # print(5,loc)  loc=('id', 'com.longfor.app.turbo.beta.debug:id/tv_ok')
            WebDriverWait(self.driver,100,0.5).until(
                Ec.visibility_of_element_located(loc)
            )
            return self.driver.find_element(*loc)
        except Exception:
            self.logger.error("未找到元素：%s 请检查！" %loc[1])
            screen_shot_path = self.get_screen("../screen_shot/")
            self.logger.error("截图路径：%s "%screen_shot_path)

    def send_keys(self,loc,value,clear_first=True,click_first=True):
        try:
            loc = getattr(self,"_%s" %loc)    #返回self对象的属性值
            print(3,loc,click_first,clear_first)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.logger.error("未找到元素：%s 请检查！" % loc[1])
            screen_shot_path = self.get_screen("../screen_shot/")
            self.logger.error("截图路径：%s "%screen_shot_path)

    def is_toast_exist(self,text):
        '''is toast exist, return True or False
                :Agrs:
                    - text   - 页面上看到的文本内容
                :Usage:
                    is_toast_exist("看到的内容")
                '''
        try:
            toast_loc = (By.XPATH,'.//*[contains(@text,"%s")]'%text)
            WebDriverWait(self.driver,100,0.5).until(
                Ec.presence_of_element_located(toast_loc)
            )
            return True
        except Exception as e:
            print(e)
            self.logger.error("未找到元素：%s 请检查！"%text)
            screen_shot_path = self.get_screen("../screen_shot/")
            self.logger.error("截图路径：%s "%screen_shot_path)
            return False

    def get_screen(self,screenshot_path):
        screenshot_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        screenshot_name = screenshot_path + screenshot_time + ".png"
        self.driver.get_screenshot_as_file(screenshot_name)
        return screenshot_name