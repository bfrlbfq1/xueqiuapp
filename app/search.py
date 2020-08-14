"""
查询页
"""
from selenium.webdriver.common.by import By

from app.searchdetailpage import SearchDetailPage
from page.basepage import BasePage


class Search(BasePage):
    def search_input(self,name):
        self.find_send_key(By.ID, f'{name}', 'com.xueqiu.android:id/search_input_text')
        return self
    def search_click(self,name):
        self.find_click(By.XPATH,f'//*[@resource-id="com.xueqiu.android:id/listview"]//*[@text="{name}"]')
        return SearchDetailPage(self.driver)