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


parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('-id','--id', required=True,  type=int)

args = vars(parser.parse_args())
# print("Hi there {}, it's nice to meet you!".format(args["id"]))

config = {
    'user': 'root',
        'password': 'root',
            'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
                'database': 'scrapper',
                    'raise_on_warnings': True,
}
try:
    mydb = mysql.connector.connect(**config)

    mycursor = mydb.cursor()

    sqlSelect = "SELECT * FROM base WHERE id="+str(args['id'])
    mycursor.execute(sqlSelect)

    myresult = mycursor.fetchone()

    # for x in myresult:

    frm_date = myresult[1]
    to_date = myresult[2]
    # print("%s",myresult[1])

    options = FirefoxOptions()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(30)
    # driver.maximize_window()

    driver.get('https://main.sci.gov.in/judgments')
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    time.sleep(2)

    driver.find_element_by_link_text('Judgment Date').click()

    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    driver.find_element_by_id('JBJfrom_date').clear()
    driver.find_element_by_id('JBJfrom_date').send_keys(frm_date)
    time.sleep(1)

    driver.find_element_by_id('JBJto_date').clear()
    driver.find_element_by_id('JBJto_date').send_keys(to_date)

    element = driver.find_element_by_id('captcha')
    location = element.location

    size = element.size
    driver.save_screenshot('screenshot.png')

    captcha = driver.find_element_by_id('ansCaptcha')
    captcha.clear()

    captcha_text = get_captcha_text(location, size)
    captcha.send_keys(captcha_text)
    driver.find_element_by_id('v_getJBJ').click()

    time.sleep(5)

    output = driver.find_element_by_id('JBJ')

    source_code = output.get_attribute("outerHTML")
    print(source_code)
    #https://medium.com/@vineet_c/using-tesseract-to-solve-captcha-while-logging-in-to-a-website-with-selenium-899a810cf14

    sql = "UPDATE base SET data=%s WHERE id=%s"
    val = (source_code,str(args['id']))
    mycursor.execute(sql, val)
    mydb.commit()
    driver.quit()
except Exception as err:
    print('ERROR: %sn' % str(err))
    mydb.close()
    driver.quit()
