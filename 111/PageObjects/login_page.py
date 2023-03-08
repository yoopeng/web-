from Common.basepage import *
from PageLocators.login_page_locators import LoginPageLocator as loc

class LoginPage(BasePage):
    #登录操作
    def login(self,username,pwd):

        #页面操作说明
        msg='登录页面-登录'
        # 等待输入用户名输入框出现
        self.wait_eleVisible(loc.username,doc=msg)
        #输入用户名
        self.inpu_text(loc.username,username,msg)
        #输入密码
        self.inpu_text(loc.password,pwd,msg)
        #点击登录
        self.click_element(loc.loginbutten,msg)

    #获取弹框信息
    def get_login_error_msg(self,action):
        return self.alert_action(action)



