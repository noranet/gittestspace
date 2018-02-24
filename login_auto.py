# encoding: utf-8
from selenium import webdriver
import time
import os
#chromedriver="D:\program\ChromeDriver\chromedriver.exe"
def login():
    dr=webdriver.Chrome()
    dr.get('http://mail.163.com')
    #dr.maximize_window()
    #time.sleep(10)
    nowhandle = dr.current_window_handle
    dr.implicitly_wait(10)
    dr.switch_to.frame(0)
    while 1:
        start=time.clock()
        try:
            email=dr.find_element_by_name('email')
            #email=dr.find_element_by_xpath('//*[@id="auto-id-1519462802552"]')
            print '已定位到元素'
            end=time.clock()
            break
        except:
            print '还没定位到元素'
    print '定位耗时：'+str(end-start)
    #email=dr.find_element_by_xpath('//*[@id="auto-id-1519462802552"]')
    dr.switch_to.frame('x-URS-iframe')
    email.send_keys('nnnnn')
    password=dr.find_element_by_name('password')
    password.send_keys('111111')
    login_btn=dr.find_element_by_name('dologin')
    login_btn.click()
    time.sleep(10)
    dr.close()
if __name__=='__main__':
    login()
