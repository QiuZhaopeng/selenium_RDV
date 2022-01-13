from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
import jsonlines
import re
import time
import selenium
import sys


#chrome_driver = "E:\sw_projects\huawei_project\chromedriver\chromedriver.exe"
chrome_driver = "C:\\Users\\qiu_z\\Downloads\\chromedriver_win32\chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument('user-data-dir=E:\\sw_projects\\tmp') 
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"')


browser = webdriver.Chrome(executable_path=chrome_driver, options=chrome_options)


from playsound import playsound

class RDV_checker():

    def __init__(self):
        self.id = 3

    def check(self):

        url = "https://www.val-doise.gouv.fr/booking/create/11404" #"http://www.hauts-de-seine.gouv.fr/booking/create/11532"
        #url = "http://www.hauts-de-seine.gouv.fr/booking/create/11532"
        browser.get(url)
        time.sleep(2)
        js="var q=document.documentElement.scrollTop=100000"  
        browser.execute_script(js)  
        time.sleep(1)
        try:
            checkbox = browser.find_element_by_xpath("//input[@id='condition']")   
            submitbutton = browser.find_element_by_xpath("//input[@name='nextButton']")   

            checkbox.click()
            time.sleep(0.5)
            submitbutton.click()
            time.sleep(4)
            '''
            try:
                planning_Booking = browser.find_element_by_xpath("//div[@id='planning_Booking']") 
                playsound("E:\Animals-Maroon_5.mp3")
                sleep(1000)
                return 1
            except Exception as e:
                return 0
            '''
            try:
                inner_booking = browser.find_element_by_xpath("//div[@id='inner_Booking']") 
                
                if "existe plus de plage" in inner_booking.text:
                    #print("playing music")
                    #playsound("cheerful-whistling.mp3")
                    
                    return 0
                else:
                    return 1
            except Exception as e:
                sleep(2000)
                
        except Exception as e:
            return 0



if __name__ == "__main__":

    myEngine = RDV_checker()
    while True:
        res = myEngine.check()
        if res == 1:
            playsound("cheerful-whistling.mp3")
        else:
            print("There is no time slot for the moment, I will try again in 1 minute")
            pass
        time.sleep(140)