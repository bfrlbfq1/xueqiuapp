from selenium.webdriver.common.by import By

from app.market import Market
from page.basepage import BasePage

"""
首页
"""


class MainPage(BasePage):
    def goto_market(self):
        self.find_click(By.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]')
        return Market(self.driver)
    def goto_back(self):
        self.driver.implicitly_wait(30)
        self.find(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/post_status"]').click()
        self.find(By.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()
        return
