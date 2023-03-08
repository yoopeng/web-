import pytest
from selenium import webdriver
from time import sleep
#
# def setup_moduel():
#     print('q')
#
# def teardown_module():
#     print('w')


class Testaa:
    @pytest.fixture()
    def openweb(self):
        print('打开浏览器')
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        sleep(2)
        yield self.driver
        sleep(2)
        self.driver.quit()
        print('关闭-----------------------')

    #第一种使用
    @pytest.mark.usefixtures('openweb')
    def test_aa(self):
        self.driver.get('https://www.baidu.com')

   #第二种使用
    def test_aa(self,openweb):
        self.driver.get('https://www.baidu.com')
    # @pytest.fixture(autouse=False)
    # def login(self):
    #     print('aaaaaaaaaaaa')
    #     yield
    #     print('bbbbbbbbbb')
    #
    # def test_a(self,login):
    #      print('1')
    #
    def test_b(self):
        print('2')



if __name__ == '__main__':
    pytest.main(['-vs','test_ee.py'])