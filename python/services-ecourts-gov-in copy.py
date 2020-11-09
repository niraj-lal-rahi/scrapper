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
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



def get_captcha_text(location, size):
    # pytesseract.pytesseract.tesseract_cmd = 'path/to/pytesseract'
    im = Image.open('screenshot.png')
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('screenshot.png')
    # response = requests.get("http://main.sci.gov.in/php/captcha.php")
    captcha_text = image_to_string(Image.open('screenshot.png'))
    return captcha_text


def get_captcha_image(driver):
    element = driver.find_element_by_id('captcha_image')
    location = element.location

    size = element.size
    driver.save_screenshot('screenshot.png')

    return get_captcha_text(location,size)

parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('-id','--id', required=True,  type=int)

args = vars(parser.parse_args())
print("Hi there {}, it's nice to meet you!".format(args["id"]))

config = {
    'user': 'root',
        'password': 'root',
            'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
                'database': 'scrapper',
                    'raise_on_warnings': True,
}

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get('https://services.ecourts.gov.in/ecourtindia_v4_bilingual/cases/s_orderdate.php?state=D&state_cd=26&dist_cd=8')
WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

time.sleep(2)

# element = driver.find_element_by_id('captcha_image')
# location = element.location

# size = element.size
# driver.save_screenshot('screenshot.png')
captcha_text = get_captcha_image(driver)
courtComplex = Select(driver.find_element_by_id("court_complex_code")).select_by_value('1@1,2,3,4@N')

fromDate = driver.find_element_by_id('from_date').send_keys('02-09-2020')
toDate = driver.find_element_by_id('to_date').send_keys('03-09-2020')

captcha = driver.find_element_by_id('captcha')
captcha.clear()

i=0

while i<10 :

    print(i)
    captcha.send_keys(captcha_text)

    driver.execute_script("validate();")
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                        'Timed out waiting for PA creation ' +
                                        'confirmation popup to appear.')

        alert = driver.switch_to.alert

        if(alert.accept()) :

            captcha_text = get_captcha_image(driver)
            captcha.send_keys(captcha_text)

            driver.execute_script("validate();")

            server_error_msg = driver.find_element_by_id('errSpan')
            if server_error_msg.is_displayed() :
                i=i+1
        else:
            break
    except TimeoutException:
        server_error_msg = driver.find_element_by_id('errSpan')
        if server_error_msg.is_displayed() :
            i=i+1
        else :
            break


time.sleep(5)

output = driver.find_element_by_id('showList3')
source_code = output.get_attribute("outerHTML")
print(source_code)

