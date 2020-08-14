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
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
    @black_handle
    def find(self, by, locator=None):
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