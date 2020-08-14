from app.app import App


class TestXueQiu:
    def setup_class(self):
        self.app=App()
        self.start=self.app.start()
    def test_xueqiu(self):
        ell =self.start.goto_main_app().goto_market().goto_search().search_input('阿里巴巴-SW').search_click('阿里巴巴-SW').optional('阿里巴巴-SW').goto_toaset('阿里巴巴-SW')
        assert ell==True