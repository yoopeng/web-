from selenium import webdriver
import unittest
from PageObjects.login_page import *
from TestDatas import login_datas as LD
from time import sleep
import ddt
from unittestreport import TestRunner

def setUpModule():#********模块级别的初始化方法setUpModule**********
    pass
def tearDownModule():#********模块级别的初始化方法tearDownModule**********
    pass

@ddt.ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):#**********类级别的初始化方法setUpClass************
        pass
    @classmethod
    def tearDownClass(cls):#**********类级别的初始化方法tearDownClass************
        pass

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://a17.gwccoin.com/app5/login.php')
        self.driver.maximize_window()
        self.lg=LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    #登录成功
    @ddt.data(LD.success_datas)       #LD.success_datas是字典就不用就*
    def test_login_seccess(self,data):
        #输入用户名，密码，点击登录
        self.lg.login(data['username'],data['password'])
        sleep(1)

    # #登录失败
    # @ddt.data(*LD.error_datas)         #LD.error_datas是列表
    # def test_login_error(self,data):
    #     self.lg.login(data['username'],data['password'])
    #     self.assertEqual(self.lg.get_login_error_msg('文本'),data['msg'])


if __name__ == '__main__':
    unittest.main()



