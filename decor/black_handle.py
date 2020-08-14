"""
装饰器
"""
from selenium.webdriver.common.by import By


def black_handle(fun):
    def element_wrapper(*args,**kwargs):
        _err_num = 0
        _max_err_num = 3
        _back_list = {
            (By.ID, 'com.xueqiu.android:id/iv_close')
        }
        from page.basepage import BasePage
        instance:BasePage = args[0]
        try:
            element =fun(*args,**kwargs)
            _err_num=0
            instance.implicitly_wait(3)
            return element
        except Exception as e:
            if _err_num>_max_err_num:
                _err_num = 0
                raise e
            _err_num+=1
            for ele in _back_list:
                eles=instance.finds(ele)
                if len(eles)>0:
                    eles[0].click()
                    return element_wrapper(*args,**kwargs)
            raise ValueError('无黑名单中的元素')
    return element_wrapper