from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
import logging.config

logging.config.dictConfig()
from appium import webdriver
import base64
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.1.2"
desired_caps["deviceName"] = "127.0.0.1:62001"
desired_caps["appPackage"] = "com.longfor.app.turbo.beta.debug"
desired_caps["appActivity"] = "com.longfor.app.turbo.business.login.LoginByAuthCodeActivity"
# 如果无法输入中文需要加入以下两行代码
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)

# 隐式等待
# driver.implicitly_wait(5)

toast_loc = (By.XPATH, ".//*[contains(@text,'%s')]" %"特别提示")
if WebDriverWait(driver,5,0.5).until(Ec.visibility_of_element_located(toast_loc)):
    driver.find_element_by_id("com.longfor.app.turbo.beta.debug:id/tv_ok").click()

time.sleep(5)
