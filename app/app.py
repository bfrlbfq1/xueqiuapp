from app.mainpage import MainPage
from page.basepage import BasePage
from appium import webdriver

"""
启动页
"""


class App(BasePage):
    def start(self):
        if self.driver == None:
            cap_des = {}
            cap_des['platformName'] = 'android'
            # cap_des['deviceName'] = '127.0.0.1:7555'
            cap_des['appPackage'] = 'com.xueqiu.android'
            cap_des['appActivity'] = '.view.WelcomeActivityAlias'
            cap_des['noReset'] = 'true'
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap_des)
        else:
            self.driver.launch_app()
        self.implicitly_wait(10)
        return self

    def goto_main_app(self):
        return MainPage(self.driver)
