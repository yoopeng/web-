from selenium.webdriver.common.by import By

class LoginPageLocator:
    #元素定位
    #用户名输入框
    username=(By.XPATH,'//*[@id="usern"]')
    #密码输入框
    password=(By.XPATH,'//*[@id="pwd"]')
    #登录按钮
    loginbutten = (By.XPATH, '/html/body/div[1]/div[2]/div/form/div[4]/button')