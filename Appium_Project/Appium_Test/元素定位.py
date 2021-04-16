from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec

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

# 定位元素
# driver.find_element_by_id("com.android.settings:id/search").click()
# time.sleep(5)
# driver.find_element_by_class_name("android.widget.EditText").send_keys("Hello World!!!")
# time.sleep(5)
# driver.find_element_by_xpath('//*[@content-desc="收起"]').click()

# 隐式等待
driver.implicitly_wait(5)


# # 显式等待,10s之内，每2s查到一次指定元素
# WebDriverWait(driver,10,2).until(lambda x:x.find_element_by_xpath('//*[@content-desc="收起"]')).click()

# # 元素操作方法，点击、输入、清空
# driver.find_element_by_id("com.android.settings:id/search").click()
driver.find_element_by_class_name("android.widget.EditText").send_keys("Hello World!!!")
# driver.find_element_by_class_name("android.widget.EditText").clear()
# driver.find_element_by_class_name("android.widget.EditText").send_keys("你好")

# # 获取元素文本、位置、大小
# print(driver.find_element_by_class_name("android.widget.TextView").text)
# print(driver.find_element_by_id("com.android.settings:id/search").location)
# print(driver.find_element_by_id("com.android.settings:id/search").size)

# # 根据属性名获取属性值
# els = driver.find_elements_by_class_name("android.widget.TextView")
# for el in els:
#     print(el.get_attribute("text"))

# # swipe滑动(起始X坐标，起始Y坐标，结束X坐标，结束Y坐标)
# driver.swipe(100,500,100,100)

# # scroll滑动
# destination_el=driver.find_element_by_xpath('//*[@text="WLAN"]')
# origin_el = driver.find_element_by_xpath('//*[@text="存储"]')
# driver.scroll(origin_el,destination_el,3000)
# # 拖拽
# driver.drag_and_drop(origin_el,destination_el)

# # 轻敲tap
# ele = driver.find_element_by_xpath('//*[@text="WLAN"]')
# TouchAction(driver).tap(ele).perform()

# # 长按press和抬起release
# ele = driver.find_element_by_xpath('//*[@text="WLAN"]')
# TouchAction(driver).press(ele).release().perform()

# # 等待wait
# ele_one = driver.find_element_by_xpath('//*[@text="WLAN"]')
# TouchAction(driver).press(ele_one).release().perform()
# ele_two = driver.find_element_by_class_name("android.widget.RelativeLayout")
# TouchAction(driver).press(ele_two).wait(2000).release().perform()

# # 长按long_press
# TouchAction(driver).long_press(el=ele_one,duration=3000).perform()

# # 移动move_to(el=None,x=None,y=None)
# TouchAction(driver).move_to(el=None,x=None,y=None)

# # 获取手机分辨率
# driver.get_window_size()
# # 截图
# driver.get_screenshot_as_file("screen.png")

# 获取当前网络状态
# print(driver.network_connection)

# # 设置当前网络状态
# driver.set_network_connection(connection_type=1)

# # 发送键到设备
# driver.press_keycode(24)
# time.sleep(2)
# driver.press_keycode(24)
# time.sleep(2)
# driver.press_keycode(24)
# time.sleep(2)
# driver.press_keycode(4)
# time.sleep(2)
# driver.press_keycode(25)
# time.sleep(2)
# driver.press_keycode(25)
# time.sleep(2)

# # 操作通知栏
# driver.open_notifications()
# time.sleep(2)
# driver.press_keycode(4)

time.sleep