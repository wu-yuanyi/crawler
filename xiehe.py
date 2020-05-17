# -*- coding: utf-8 -*-
"""
Created on the heartbreak moment
@author: wuyuanyi
"""
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# login
driver = webdriver.Chrome(r'C:\Users\Public\WYYSB\machine\chromedriver.exe')
driver.get("http://10.1.5.22/lims")
time.sleep(5)

username = driver.find_element_by_name('token')
username.send_keys('chenyuan')
password = driver.find_element_by_name('password')
password.send_keys('Az123456')
submit = driver.find_element_by_name('submit')
submit.click()
time.sleep(5)

# New AIRA III
driver.get("http://10.1.5.22/lims/!equipments/equipment/index.8.reserv")
time.sleep(5)


button_list = driver.find_elements_by_class_name('button')
for item in button_list:
    if item.text.startswith('下周'):
        item.click()
        break
time.sleep(5)

daynum = (datetime.date.today().weekday()+1)%7
hour_cell = "td.hour_cell.R32C" + str(daynum)
#hour_cell = "td.hour_cell.R12C4" 
print(hour_cell)


time.sleep(3)
driver.execute_script('window.scrollBy(0,1000)')
time.sleep(2)

print('ok!')

def roll():
    print("roll")
    order = driver.find_element_by_css_selector(hour_cell)
    actionChains = ActionChains(driver)
    actionChains.double_click(order).perform()
    #actionChains.double_click(order).perform()
    machine_flag = True
    while True:
        time.sleep(0.4)
        alter = None
        occupy = None
        try:
            alter = driver.switch_to_alert()
        except:
            pass
        if alter != None:
            print(alter.text)
            alter.accept()
            order = driver.find_element_by_css_selector(hour_cell)
            actionChains = ActionChains(driver)
            actionChains.double_click(order).perform()
        else:
            try:
                occupy = driver.find_elements_by_css_selector('li')
            except:
                pass
        if occupy != None:
            if len(occupy) > 4:
                if occupy[4].text == '您没有权限修改他人预约！':
                    print('对不起阿鲸，没抢到机器')
                    machine_flag = False
                    break
            else:
                break

    if machine_flag:
        # time
        try:
            point_list = driver.find_elements_by_css_selector('input.text.date')
            #start = point_list[0]
            end = point_list[1]
            end.click()
            hour=driver.find_element_by_xpath("/html/body/div/div[4]/a")
            hour.click()
            hour.send_keys('18')
            min=driver.find_element_by_xpath("/html/body/div/div[5]/a")
            min.click()
            min.send_keys('59')

            #confirm
            save = driver.find_element_by_name('save')
            save.click()
            print('元一已经帮您预约机器')
            return 'OK'
        except:
            roll()

roll()     
