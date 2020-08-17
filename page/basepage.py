import json
import logging

import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from decor.black_handle import black_handle

class BasePage:
    # _err_num=0
    # _max_err_num=3
    # _back_list={
    #     (By.ID,'com.xueqiu.android:id/iv_close')
    # }
    _params={}
    logging.basicConfig(level=logging.INFO)
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
    @black_handle
    def find(self, by, locator=None):
        logging.info('self.driver.find_element(*by):'+by+'***'+locator)
        # try:
        if locator == None:
            result= self.driver.find_element(*by)
        else:
            result= self.driver.find_element(by, locator)
        # self._err_num=0
        return result
        # except Exception as e:
        #     if self._err_num>self._max_err_num:
        #         self._err_num = 0
        #         raise e
        #     self._err_num+=1
        #     for ele in self._back_list:
        #         eles=self.finds(ele)
        #         if len(eles)>0:
        #             eles[0].click()
        #             return self.find(by,locator)
        #     raise e

    def finds(self, by, locator=None):
        if locator == None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locator)

    def find_click(self, by, locator=None):
        if locator == None:
            return self.driver.find_element(*by).click()
        else:
            return self.driver.find_element(by, locator).click()

    def find_send_key(self, by, value, locator=None):
        if locator == None:

            return self.driver.find_element(*by).send_keys(value)
        else:
            return self.driver.find_element(by, locator).send_keys(value)
    def find_wait(self,by,locator):
        WebDriverWait(self.driver,10).until(lambda x:x.find_element(by,locator))
    def implicitly_wait(self,no):
        self.driver.implicitly_wait(no)
    def step_yaml(self,path,name):
        with open(path,encoding='utf-8') as f:
            datas = yaml.safe_load(f)[name]
        row =json.dumps(datas)
        for key,value in self._params.items():
            row=row.replace('${'+key+'}',value)
        datas=json.loads(row)
        logging.info('datas:'+datas)
        for data in datas:
            if 'by' in data.keys():
                step=self.find(data['by'], data['locator'])
            if 'locator' in data.keys():
                if 'click'==data['action']:
                    step.click()
                if 'send' ==data['action']:
                    print(step)
                    step.send_keys(data['value'])

    def save_screenshot(self,path):
        return self.driver.save_screenshot(path)