# -*- coding: utf-8 -*-

import sys
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

chromeOptions = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chromeOptions)

def parse_out_tag(html):
    i = 0
    new_html = ""

    while 44:
        if i + 1 >= len(html):
            break
        if html[i] == '>' and html[i + 1] != '<':
            while 44:
                if i >= len(html):
                    break
                if html[i] == '<':
                    break
                new_html += html[i]
                i += 1
        i += 1
    return new_html

def get_city(fbid):
    driver.get("http://www.facebook.com/profile.php?id=" + fbid + "&sk=about&section=living")
    html = driver.page_source
    city = ""
    if "fbProfileEditExperiences" in html:
        html = html.split("fbProfileEditExperiences")
        if len(html) >= 3:
            city = html[1] + html[2]
        else:
            city = html[1]
        city = city.split("pagelet_timeline_medley_friends")[0]
        city = parse_out_tag(city)
    return city

def get_job(fbid):
    driver.get("http://www.facebook.com/profile.php?id=" + fbid + "&sk=about&section=education")
    html = driver.page_source
    job = ""
    if "fbProfileEditExperiences" in html:
        html = html.split("fbProfileEditExperiences")
        if len(html) >= 3:
            job = html[1] + html[2]
        else:
            job = html[1]
        job = job.split("pagelet_timeline_medley_friends")[0]
        job = parse_out_tag(job)
    return job

def get_realname(fbid):
    realname = ""
    driver.get("http://www.facebook.com/profile.php?id=" + fbid)
    html = driver.page_source
    realname = html.split("fb-timeline-cover-name")[1]
    realname = realname.split("</")[0]
    realname = realname[2:]
    return realname

def get_id(victim):
    fbid = ""
    driver.get("https://www.facebook.com/" + victim)
    html = driver.page_source
    if "entity_id" in html:
        fbid = html.split("entity_id")[1]
        fbid = fbid.split("}]")[0]
        fbid = fbid[3:]
        fbid = fbid[:-1]
    return fbid

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

def main(username, passwd, victim):
    global uid
    print("--> " + victim)
    log_to_fb(driver, username, passwd)
    uid = get_id(victim)
    print("--> Uid : " + uid)
    realname = get_realname(uid)
    print("--> Name: " + realname)
    job = get_job(uid)
    print("--> Job : " + job)
    city = get_city(uid)
    print("--> City : " + city)
    
def print_help():
    print("You must enter a valid name!")
    
if __name__ == "__main__":

    if len(sys.argv) < 4:
        print_help()
        sys.exit()
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
