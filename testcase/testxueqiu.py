import pytest
import yaml

from app.app import App


class TestXueQiu:
    def setup_class(self):
        self.app=App()
        self.start=self.app.start()
    @pytest.mark.parametrize('stock_name',yaml.safe_load('../data/data.yaml',encoding='utf-8'))
    def test_xueqiu(self,stock_name):
        ell =self.start.goto_main_app().goto_market().goto_search().search_input(stock_name).search_click(stock_name).optional(stock_name).goto_toaset(stock_name)
        assert ell==True