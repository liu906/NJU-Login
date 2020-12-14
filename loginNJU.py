import os

from selenium import webdriver

import time, subprocess

def login():

    # You most certainly want to change this
    url = "http://p.nju.edu.cn/portal/index.html"

    # profile = webdriver.FirefoxProfile()
    # Set a user agent string to help parse webserver logs easily
    # profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 selenium.py")
    # browser = webdriver.Firefox(firefox_profile=profile,executable_path="/home/lau/geckodriver")
    browser = webdriver.Firefox(executable_path="/home/lau/geckodriver")
    
    browser.get(url)
    time.sleep(1)

    # The element names will likely be different for your application,
    # therefore change accordingly
    user = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    print("Element is visible? " + str(user.is_displayed()))
    print("Element is visible? " + str(password.is_displayed()))
    # Clear the input fields
    user.clear()
    password.clear()
    user.send_keys("DZ1933019")
    password.send_keys("dh/SB/321")
    time.sleep(1)
    browser.find_element_by_id("loginBtn").click()

    # Keep the page loaded for 8 seconds
    time.sleep(8)

    # Log out
    # The element IDs will likely be different for your application,
    # therefore change accordingly
    # browser.find_element_by_id("logout_link").click()
    # time.sleep(2)
    # browser.find_element_by_id("dialog_button_ok").click()
    # time.sleep(1)

    browser.delete_all_cookies()
    browser.close()
            
exit_code = os.system('ping baidu.com -c2 -W1')
if exit_code:
    print("go to login")
    login()

