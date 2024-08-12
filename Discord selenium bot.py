from selenium import webdriver 
import time
from selenium.webdriver.common.keys import Keys
import random
browser = webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver.exe")

browser.get(input("Enter your discord channel link : "))
time.sleep(2)
search_btn = browser.find_element_by_name('email')
search_btn.send_keys(input("Enter gmail : "))

time.sleep(2)
search_btn1 = browser.find_element_by_name('password')
search_btn1.send_keys(input("Enter password : "))

time.sleep(2)
search_btn2 = browser.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]')
search_btn2.click()
word = ["higher","lower"]
rand = random.choice(word)
while True :
 time.sleep(40)
 search_btn3 = browser.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]/div')
 search_btn3.send_keys("pls fish")
 search_btn3.send_keys(Keys.ENTER)
 time.sleep(2)
 search_btn4 = browser.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]/div')
 search_btn4.send_keys("pls hunt")
 search_btn4.send_keys(Keys.ENTER)
 time.sleep(2)
 search_btn5 = browser.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]/div')
 search_btn5.send_keys("pls dig")
 search_btn5.send_keys(Keys.ENTER)
 time.sleep(2)
 search_btn6 = browser.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]/div')
 search_btn6.send_keys("pls beg")
 search_btn6.send_keys(Keys.ENTER)
