"""
搜索详情页面
"""
from selenium.webdriver.common.by import By

from page.basepage import BasePage


class SearchDetailPage(BasePage):
    def optional(self,name):
        self.find_click(By.XPATH,f'//*[contains(@resource-id,"stock_item_container")]//*[@text="{name}"]/../..//*[@text="加自选"]')
        return self
    def goto_toaset(self,name):
        # self.find(By.XPATH,'//*[@class="android.widget.Toast"]')
        # reslut=self.find_wait(By.XPATH,'//*[contains(@text,“添加成功”)]')
        ele =self.finds(By.XPATH,f'//*[contains(@resource-id,"stock_item_container")]//*[@text="{name}"]/../..//*[@text="加自选"]')
        reslut =len(ele)
        return reslut==0
