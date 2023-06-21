#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

username = 'ee22b151'
password = 'yourPassworD'

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://netaccess.iitm.ac.in/account/login")

uname = driver.find_element("id", "username").send_keys(username)
pword = driver.find_element("id", "password").send_keys(password)
driver.find_element('id', 'submit').click()

driver.get('https://netaccess.iitm.ac.in/account/approve')
approve_duration = driver.find_element('id', 'radios-2').click() # radios-1 for duration as 1 day 
authorize_btn = driver.find_element('id', 'approveBtn').click()

driver.quit()
