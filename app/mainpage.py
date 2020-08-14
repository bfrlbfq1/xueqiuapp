import yaml
from selenium.webdriver.common.by import By

from app.market import Market
from page.basepage import BasePage

"""
首页
"""


class MainPage(BasePage):

    def goto_market(self):
        # with open('../data/main.yaml',encoding='utf-8') as f:
        #     datas = yaml.safe_load(f)
        # for data in datas:
        #     if 'by' in data.keys():
        #         step=self.find(data['by'], data['locator'])
        #     if 'locator' in data.keys():
        #         if 'click'==data['action']:
        #             step.click()
        self.step_yaml('../data/main.yaml')
        return Market(self.driver)
    def goto_back(self):
        self.driver.implicitly_wait(30)
        self.find(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/post_status"]').click()
        self.find(By.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]').click()
        return
