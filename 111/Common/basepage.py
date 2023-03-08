#封装基本操作，定位，点击，输入，执行日志，异常处理，失败截图等
import logging.config
import warnings
import logging
import time,os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib #发送邮件模板
from email.mime.text import MIMEText #定义邮件内容
from email.header import Header #定义邮件标题
import MySQLdb.cursors #mysql数据库
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class BasePage:
    # 日志配置
    CON_LOG = '../config/log.conf'
    logging.config.fileConfig(CON_LOG)
    logging = logging.getLogger()
    # 如日志出现乱码，添加
    warnings.simplefilter("ignore", ResourceWarning)

    def __init__(self,driver):
        self.driver=driver

    #获取当前时间
    def gettime(self):
        self.now=time.strftime('%Y-%m-%d %H:%M:%S')
        return self.now

    #截图
    def get_screenshot(self,doc=''):
        '''
        :param name: 模块加操作名
        :return:
        '''
        time=self.gettime()
        #截图存放路径
        path=os.path.dirname(os.path.dirname(__file__))+'/Output/screenshot/'
        #图片名
        opath=path+'%s_%s.png'%(doc,time)
        self.driver.get_screenshot_as_file(opath)
        logging.info('截图成功，图片名为%s'%doc)


    #等待元素可见
    def wait_eleVisible(self,loc,doc=''):
        '''
        :param loc:
        :param times:
        :param poll_frequency:
        :param doc: 模块加操作名
        :return:
        '''

        logging.info('等待元素 {} 可见'.format(loc))
        try:
            WebDriverWait(self.driver,5,0.5).until(EC.visibility_of_element_located(loc))
        except:
            logging.exception('等待元素 {} 可见失败！！！'.format(loc))
            #截图
            self.get_screenshot(doc)
            raise

    #等待元素存在
    def wait_elePresence(self, loc, doc=''):
        '''
        :param loc:
        :param times:
        :param poll_frequency:
        :param doc: 模块加操作名
        :return:
        '''

        logging.info('等待元素 {} 存在'.format(loc))
        try:
            WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located(loc))
        except:
            logging.exception('等待元素 {} 存在失败！！！'.format(loc))
            # 截图
            self.get_screenshot(doc)
            raise

    #查找元素
    def find_element(self,loc,doc=''):
        logging.info('查找元素{}'.format(loc))
        try:
            return self.driver.find_element(*loc)
        except:
            logging.exception('查找元素失败%s'%loc)
            self.get_screenshot(doc)
            raise

    #点击操作
    def click_element(self,loc,doc=''):
        #定位元素
        element=self.find_element(loc,doc)
        #点击操作
        logging.info('点击元素{}'.format(loc))
        try:
            element.click()
        except:
            logging.exception('元素点击失败！！！！')
            #截图
            self.get_screenshot(doc)

    #输入操作
    def inpu_text(self,loc,text,doc=''):
        # 定位元素
        element = self.find_element(loc, doc)
        # 点击操作
        logging.info('输入内容{}'.format(text))
        try:
            element.send_keys(text)
        except:
            logging.exception('输入内容失败！！！！')
            # 截图
            self.get_screenshot(doc)

    #获取元素文本内容
    def get_text(self,loc,doc=''):
        #元素定位
        element=self.find_element(loc,doc)
        #获取文本内容
        logging.info('获取文本内容{}'.format(loc))
        try:
            return element.text
        except:
            logging.exception('获取文本失败！！！！！')
            #截图
            self.get_screenshot(doc)
            raise

    #获取元素属性
    def get_element_attribute(self,loc,attr,doc=''):
        #元素定位
        element=self.find_element(loc,doc)
        #获取元素属性
        logging.info('获取元素属性{}'.format(attr))
        try:
            return element.get_attribute(attr)
        except:
            logging.exception('获取元素失败')
            # 截图
            self.driver.get_screenshot_as_file(doc)
            raise

    #alert弹框处理(浏览器弹框)
    def alert_action(self,action,text=None):
        alert=self.driver.switch_to.alert
        if action=='接受':
            alert.accept()
        elif action=='取消':
            alert.dismiss()
        elif action=='文本':
            return alert.text
        elif action=='输入':
            alert.send_keys(text)

    #iframe切换
    def switch_to_frame(self,loc,doc=''):
        #元素定位
        element=self.find_element(loc,doc)
        logging.info('切换表单')
        #iframe切换
        try:
            self.driver.switch_to.frame(element)
        except:
            logging.exception('切换iframe失败')
            #截图
            self.get_screenshot(doc)
        #self.driver.switch_to.parent_frame()  切换上层表单
        #self.driver.switch_to.default_content()  切换回默认表单（最外层）

    #鼠标悬停
    def mouse_hovering(self,loc,doc=''):
        above=self.find_element(loc,doc)
        ActionChains(self.driver).move_to_element(above).perform()

    #获取Toast
    def get_Toast(self,tips,doc=''):
        msg='//*[@text="{}"]'.format(tips)
        loc=(By.XPATH,msg)
        #等待Toast存在（等待toast，一定要用存在， 可见是不行的）
        self.wait_elePresence(loc,doc=doc)
        #返回Toast文本内容
        return self.get_text(loc,doc=doc)

    #上传操作
    #滚动条
    #滚动条下拉
    def drop_down(self):
        js='var action=document.documentElement.scrollTop=100000'
        self.driver.execute_script(js)
    #滚动条上拉
    def drop_down(self):
        js='var action=document.documentElement.scrollTop=0'
        self.driver.execute_script(js)


    #窗口切换
    def switch_window(self):
        all_handles=self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])

        
    #dangqian=self.driver.current_window_handle获取当前窗口handle
    #第一种窗口切换
    def switch_window1(self,dangqian):
        all_handles=self.driver.window_handles
        for handle in all_handles:
            if handle!=dangqian:
                self.driver.switch_to.window(handle)

    # 查找最新的测试报告
    def new_report(report_dir):
        # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
        lists = os.listdir(report_dir)
        # 按时间顺序对该目录文件夹下的文件进行排序
        lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
        print('new report is: ' + lists[-1])
        file = os.path.join(report_dir, lists[-1])
        return file

    # 针对元素不可见，display=‘None’,通过js修改为block
    # select下拉框
    def displayelement(self):
        js = "docuent.querySelectorAll('select')[0].style.display='block';"
        self.driver.execute_script(js)
        # 通过id修改

    def displayelement1(self):
        js = "document.getElementById(\"txtPassword\").style.display='block';"
        self.driver.execute_script(js)
        # 通过name属性修改

    def displayelement2(self):
        js = "document.getElementByName(\"txtPassword\").style.display='block';"
        self.driver.execute_script(js)
        # 通过tagname属性修改

    def displayelement3(self):
        js = "document.getElementByTagName(\"txtPassword\").style.display='block';"
        self.driver.execute_script(js)
    #将测试报告发送邮箱
    def send_mail(new_report):
        f = open(new_report, 'rb')
        mail_content = f.read()
        f.close()

        smtpserver = 'smtp.qq.com'
        # 发送邮箱用户名密码
        user = '861025678@qq.com'
        password = 'tivovldiyccabebb'

        # 发送和接收邮箱
        sender = '861025678@qq.com'
        receives = ['15677785787@163.com', '861025678@qq.com']

        # 发送邮件主题和内容
        subject = 'Web Selenium 自动化测试报告'

        # HTML邮件正文
        msg = MIMEText(mail_content, 'html', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = ','.join(receives)

        """
        #若报错：'utf-8' codec can't decode byte 0x8f in position 0: invalid st。。。
        #请将电脑——》设置——》语言——》管理语言设置——》更改系统区域设置——》勾选Beta版。。。重启电脑即可
        """
        # 端口465
        smtp = smtplib.SMTP_SSL(smtpserver,465)

        # HELO 向服务器标识用户身份
        smtp.helo(smtpserver)
        # 服务器返回结果确认
        smtp.ehlo(smtpserver)
        # 登录邮箱服务器用户名和密码
        smtp.login(user, password)

        logging.info("Start send Email...")
        smtp.sendmail(sender, receives, msg.as_string())
        smtp.quit()
        logging.info("Send Email end!")


    #连接数据库查询数据
    def select_mysql(self,sql):
        conn = MySQLdb.connect(
            host='localhost',#数据库地址
            port=3306,#端口号
            user='root',#账号
            passwd='861025678',#密码
            db='mysql',#库名
            charset='utf8',#编码
            cursorclass=MySQLdb.cursors.DictCursor
        )
        cur = conn.cursor()#链接数据库
        cur.execute(sql)#执行sql语句
        result = cur.fetchone()#返回结果
        return result