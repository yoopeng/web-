from selenium import webdriver
import unittest
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
sleep(2)
driver.maximize_window()
driver.get("https://www.baidu.com")
sleep(2)



a=driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
ActionChains(driver).move_to_element(a).perform()
driver.implicitly_wait(10)
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# driver.find_element_by_xpath('//*[@id="search"]/form/div[2]/input').send_keys('11111111111111111111')
# WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="search_logolink"]/img')))
# sleep(2)
# driver.find_element_by_xpath('//*[@id="search"]/form/div[3]/input').click()
# sleep(2)
# all_handles=driver.window_handles
# driver.switch_to.window(all_handles[-1])
# #driver.find_element_by_xpath('//*[@id="kw"]').send_keys('22222222222222222')
# sleep(2)
# a=driver.find_element_by_xpath('//*[@id="u"]/a[2]/text()')
# ActionChains(driver).move_to_element(a).perform()
sleep(2)
driver.quit()