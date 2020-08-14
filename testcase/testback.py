from app.app import App


class TestBack:
    def setup_class(self):
        self.app=App()
        self.main =self.app.start().goto_main_app()
    def test_back(self):
        self.main.goto_back()
