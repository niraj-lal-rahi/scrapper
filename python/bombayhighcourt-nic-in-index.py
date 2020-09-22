from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint
from selenium.webdriver.support.ui import WebDriverWait
from pytesseract import image_to_string
from PIL import Image
import time
import io
#import pytesseract
import requests
import mysql.connector
import argparse
from selenium.webdriver.firefox.options import Options as FirefoxOptions




try:
    # options = FirefoxOptions()
    # options.add_argument("--headless")

    # driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    # driver.maximize_window()

    driver.get('https://bombayhighcourt.nic.in/index.html')
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    time.sleep(2)

    text_menu = 'Court Orders'
    text = "Rep. Judgment/Orders"
    menu = driver.find_element_by_xpath('//a[contains(text(),"%s")]' % text_menu)
    driver.execute_script("arguments[0].setAttribute('class','selected')", menu)

    print(menu)
    # driver.find_element_by_link_text('Court Orders').click()
    time.sleep(2)
    driver.find_element_by_xpath('//a[contains(text(),"%s")]' % text).click()
    # driver.find_element_by_link_text('Rep. Judgment/Orders').click()
except Exception as err:
    print('ERROR: %sn' % str(err))
    driver.quit()

