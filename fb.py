# -*- coding: utf-8 -*-

import sys
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chromeOptions)

def log_to_fb(driver, username, passwd):
    driver.implicitly_wait(120)
    driver.get("https://www.facebook.com/")
    time.sleep(3)
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(passwd)
    driver.find_element_by_id("loginbutton").click()

    global all_cookies

    all_cookies = driver.get_cookies()
    html = driver.page_source
 
    if "Log into Facebook" in html:
        print("--> Incorrect Username/Password")
        sys.exit()
    else:
        print("--> You are connected!")

def main(username, passwd):
    print("--> " + username)
    log_to_fb(driver, username, passwd)
    
def print_help():
    print("You must enter a valid name!")
    
if __name__ == "__main__":

    if len(sys.argv) < 3:
        print_help()
        sys.exit()
    else:
        main(sys.argv[1], sys.argv[2])
