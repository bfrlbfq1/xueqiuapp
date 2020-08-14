from selenium.webdriver.common.by import By

from app.search import Search
from page.basepage import BasePage

"""
行情页
"""


class Market(BasePage):
    def goto_search(self):
        self.find_click(By.ID, 'com.xueqiu.android:id/action_search')
        return Search(self.driver)
