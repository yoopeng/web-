import unittest
from unittestreport import TestRunner
import time,logging


now=time.strftime('%Y-%m-%d %H_%M_%S')

test_dir= '../TestCases'
#把目录的测试用例加载到容器“discover”中,组织用例
discover = unittest.defaultTestLoader.discover(test_dir)  # 匹配所有“.py”文件
    #unittest.TextTestRunner(discover).run()

logging.info('#####################################开始执行用例##########################################')
runner = TestRunner(suite=discover)
#重跑失败用例，count为重跑次数，interval为重跑间隔时间

runner.rerun_run(count=0, interval=2)

#多线程跑用例，根据一个用例文件执行一个线程
#runner.run(thread_count=3)

#发送测试报告到邮箱
# runner.send_email(host="smtp.qq.com",
#                   port=465,
#                   user="861025678@qq.com",
#                   password="tivovldiyccabebb",
#                   to_addrs=["861025678@qq.com",'zizi.zou@celnet.com.cn'])

