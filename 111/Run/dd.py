from selenium import webdriver
import unittest
from time import sleep
from ddt import *
from selenium.webdriver.common.action_chains import ActionChains #鼠标悬停
from selenium.webdriver.support.ui import WebDriverWait


def setUpModule(): #********模块级别的初始化方法setUpModule**********
    print('123')

def tearDownModule(): #********模块级别的初始化方法tearDownModule**********
    print('456')

#读取txt文件数据
def read_txt_file():
    l=[]
    with open('aa.txt','r',encoding='utf8')as file:
        for line in file.readlines():
            print(line)
            l.append(line.strip('\n').split(','))
    print(l)
    return l

@ddt
class test1(unittest.TestCase):

    @classmethod
    def setUpClass(cls): #**********类级别的初始化方法setUpClass************

        cls.driver=webdriver.Chrome()

        cls.driver.get('http://a17.gwccoin.com/app5/login.php')
        cls.driver.maximize_window()
        # cls.driver.set_window_size(222,555)
        cls.driver.implicitly_wait(2)
    @classmethod
    def tearDownClass(cls): #**********类级别的初始化方法tearDownClass************
        cls.driver.quit()

    def setUp(self) -> None: #**********单个用例的初始化方法setUp************
        pass
    def tearDown(self) -> None: #**********单个用例的初始化方法tearDown************
        pass

    #@unittest.skip('test_login_right')
    #@unittest.skipIf(a>5,"condition is not satisfied!")#如果a>5忽略此测试方法
    #@unittest.skipUnless(sys.platform.startswith("linux"), "requires Linux")
    #@data(['15677785787','216545'],['15677785787','465451'])
    @data(*read_txt_file())
    @unpack #解date包
    def test_aa(self,username,pwd):
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(pwd)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[4]/button').click()
        sleep(2)
        aa = self.driver.switch_to.alert.text
        print(aa)
        self.assertEqual(aa,'密码错误，请检查！')
        self.driver.switch_to.alert.accept()


        sleep(2)

    # def test_bb(self):
    #     self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('15677785787')
    #     self.driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('44145728585252')
    #     self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[4]/button').click()
    #     sleep(2)
    #     aa = self.driver.switch_to.alert.text
    #     print(aa)
    #     self.assertEqual(aa, '密码错误，请检查！')
    #     self.driver.switch_to.alert.accept()
    #     sleep(2)

class test2(unittest.TestCase):
    pass

if __name__ == '__main__':
     #unittest.main()

#另一种加载用例执行用例的方法
    suit = unittest.TestSuite()
    suit.addTest(test1('test_aa'))
    unittest.TextTestRunner(suit).run()

# #另一种加载用例执行用例的方法
    # test_dir='./'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='dd.py')  # 匹配所有“.py”文件
    # unittest.TextTestRunner(discover).run()