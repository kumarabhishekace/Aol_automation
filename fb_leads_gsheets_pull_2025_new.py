import gspread
import time
import pdb
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
    

def wait_by_class(Element1):
    try:
        element = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.CLASS_NAME, Element1)))
    except TimeoutException:
        print("Loading took too much time!")


def wait_by_id(Element1):
    try:
        element = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, Element1)))
    except TimeoutException:
        print("Loading took too much time!")


whatsappLinkCol = 'C'
count = 1
#driver = webdriver.Firefox(executable_path='./geckodriver')
driver = webdriver.Chrome()
driver.maximize_window()

gc = gspread.service_account(filename='credentials.json')
# or by sheet name: gc.open("TestList")
sh = gc.open_by_key("1CBJcjG7cPC-dzK0nREBprHlmiNOkLkGogmDcr-SLFE0")
#sh = gc.open("BE_YOUR_OWN_CAREER_COUNSELLOR_Webinar_13_May2020")
#Opening google sheet
pdb.set_trace()
worksheet = sh.worksheet("abhishek_test2")


def singleRowFetch():
    while True:
        count=count+1
        try:
            url = worksheet.acell(whatsappLinkCol+str(count)).value

            if (url):

                driver.get(url)
                time.sleep(3)
                wait_by_class('_3qpzV')
                send_btn = driver.find_element_by_class_name('_3qpzV')
                send_btn.send_keys(Keys.ENTER)
            else:
                driver.quit()
                print( ' - Stopped at count:' + str(count))
                break
                
                
        except Exception as e:
            print(str(e) +' - Stopped at count:' + str(count))
            pass
    

#col_values(column number)
linkList = [item for item in worksheet.col_values(3) if item]

for whatsappLink in linkList:
    try:
        count = count+1
        url = whatsappLink
        if (url):
            driver.get(url)
            time.sleep(3)
            wait_by_class('_3qpzV')
            send_btn = driver.find_elements_by_class_name('_3qpzV')
            #send_btn = driver.find_elements_by_class_name('_2HE1Z _1hRBM')
            time.sleep(3)
            #send_btn.send_keys(Keys.ENTER)
            send_btn[1].click()

            time.sleep(3)
        else:
            #driver.quit()
            print(' - empty at count:' + str(count))
            break
    except Exception as e:
        print(str(e) + ' - Following number is not a valid whatsapp number: \n' + str(url))

driver.quit()
