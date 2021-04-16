from appium import webdriver
import base64
import time

desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.1.2"
desired_caps["deviceName"] = "127.0.0.1:62001"
desired_caps["appPackage"] = "com.ss.android.article.news"
desired_caps["appActivity"] = ".activity.MainActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
# time.sleep(2)
# # 启动其他app，参数为包名和启动名
# driver.start_activity("com.android.settings",".Settings")
# time.sleep(2)
# # 获取包名输出
# print(driver.current_package)
# # 获取启动名输出
# print(driver.current_activity)
# time.sleep(2)
# driver.close_app()
# # 通过包名去判断，存在APP则卸载，不存在则通过apk文件路径安装
# if driver.is_app_installed("com.sankuai.meituan"):
#     driver.remove_app("com.sankuai.meituan")
# else:
#     driver.install_app("C:/Users/libingqing/Desktop/group-1100060404_0-meituan.apk")
# 将应用置于后台，会自动返回前台
driver.background_app(5)
driver.quit()

# 发送文件到手机
# 文件内容hello world，base64编码
# pull_data = str(base64.b64encode("hello world!".encode("utf-8")),"utf-8")
# driver.push_file("/storage/emulated/0/pust.txt",pull_data)
# time.sleep(2)
# 读取APP文件内容
# push_data = driver.pull_file("/storage/emulated/0/pust.txt")
# print(str(base64.b64decode(push_data),"utf-8"))    #b64decode:base64解码
# 获取当前屏幕内元素结构，只显示当前页屏幕所包含内容
# print(driver.page_source)