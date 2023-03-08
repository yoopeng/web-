import unittest
from HTMLTestRunner import HTMLTestRunner
import time,logging
from Common.basepage import BasePage
import sys

"""
如创建bat命令时，一定要将
path='F:\\selenium测试框架\\'
sys.path.append(path) 放到
from common.commom_fun import commom 前面
这样就不会出现The system cannot find the path specified.(系统找不到指定路径)
"""
# #方便Jenkins读取本文件路径
# path='F:\\selenium测试框架\\'
# sys.path.append(path)



#测试用例路径
test_dir= '../TestCases/'
#测试报告路径
report_dir= '../Output/report'

#把目录的测试用例加载到容器“discover”中,组织用例
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')#匹配所有“.py”文件

#获取当前时间
now=time.strftime('%Y-%m-%d %H_%M_%S')
#测试报告名字
report_name=report_dir+'/'+now+' test_report.html'
#创建测试报告并写入
with open(report_name,'wb') as file:
    #命名测试报告里的名字
    runner=HTMLTestRunner(stream=file,title='XXXXXXXXXX测试报告',description='报告')
    logging.info('start run test case....')

    #执行测试用例
    runner.run(discover)
    logging.info('end run test case....')

    # # 获取最新生成的测试报告
    # new_report = BasePage.new_report(report_dir)
    #
    # # 发送测试报告
    # BasePage.send_mail(new_report)
