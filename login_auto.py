# encoding: utf-8
from selenium import webdriver
import time
def login():
dr=webdriver.Chrome()
dr.get('http://mail.163.com')
dr.maximize_window()
time.sleep(5)
email=dr.find_element_by_name('email')
dr.switch_to.frame('x-URS-iframe')
email.send_keys('nnnnn')
password=dr.find_element_by_name('password')
password.send_keys('111111')
login_btn=dr.find_element_by_name('dologin')
login_btn.click()
time.sleep(10)
if __name__=='__main__':
    login()
