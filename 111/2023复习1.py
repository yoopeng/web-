from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import unittest
class aa(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        sleep(2)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def vvvva(self):
        self.driver.get("https://www.baidu.com")
        sleep(2)

        a=self.driver.find_element_by_xpath('//*[@id="s-user-setting-menu"]')
        ActionChains(self.driver).move_to_element(a).perform()
        self.driver.find_element_by_link_text("搜索设置").click()
        sleep(2)

if __name__ == '__main__':
    unittest.main()

    #
    # suit=unittest.TestSuite()
    # suit.addTest(aa('a'))
    # unittest.TextTestRunner(suit).run()

    #
    # testdir='./'
    # discover=unittest.defaultTestLoader.discover(testdir,pattern='2023复习1.py')
    # unittest.TextTestRunner.run(discover).run()