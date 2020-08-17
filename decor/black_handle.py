"""
装饰器
"""
import logging

import allure
from selenium.webdriver.common.by import By


def black_handle(fun):
    logging.basicConfig(level=logging.INFO)

    def element_wrapper(*args, **kwargs):
        _err_num = 0
        _max_err_num = 3
        _back_list = {
            (By.ID, 'com.xueqiu.android:id/iv_close')
        }
        from page.basepage import BasePage
        instance: BasePage = args[0]
        try:
            logging.info('run:' + fun.__name__ + '\n args: \n' + repr(args[1:]) + '\n' + repr(kwargs))
            element = fun(*args, **kwargs)
            _err_num = 0
            instance.implicitly_wait(3)
            return element
        except Exception as e:
            instance.save_screenshot('../screenshot/tmp.png')
            with open('../screenshot/tmp.png', 'rb') as f:
                connent = f.read()
            allure.attach(connent,attachment_type=allure.attachment_type.PNG)
            logging.error('进入黑名单：'+fun.__name__+'\n args:'+repr(args[1:]))
            if _err_num > _max_err_num:
                _err_num = 0
                raise e
            _err_num += 1
            for ele in _back_list:
                eles = instance.finds(ele)
                if len(eles) > 0:
                    eles[0].click()
                    return element_wrapper(*args, **kwargs)
            raise ValueError('无黑名单中的元素')

    return element_wrapper
