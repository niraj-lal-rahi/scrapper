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
print("Hi there {}, it's nice to meet you!".format(args["id"]))

config = {
    'user': 'root',
        'password': 'root',
            'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
                'database': 'scrapper',
                    'raise_on_warnings': True,
}

mydb = mysql.connector.connect(**config)

mycursor = mydb.cursor()

sqlSelect = "SELECT * FROM base WHERE id="+str(args['id'])
mycursor.execute(sqlSelect)

myresult = mycursor.fetchone()

# for x in myresult:

frm_date = myresult[1]
to_date = myresult[2]
# print("%s",myresult[1])
try:
    #options = FirefoxOptions()
    #options.add_argument("--headless")

    #driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    # driver.maximize_window()

    driver.get('https://main.sci.gov.in/daily-order')
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    time.sleep(2)

    driver.find_element_by_link_text('ROP Date').click()

    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    driver.find_element_by_id('JBJfrom_date').clear()
    driver.find_element_by_id('JBJfrom_date').send_keys(frm_date)
    time.sleep(1)
    #selectMonth = driver.find_element_by_xpath('//select[@class="ui-datepicker-month"]')
    #for option in selectMonth.find_elements_by_tag_name('option'):
    #    if option.text == 'Aug':
    #        option.click()
    #        break
    #
    #selectYear = driver.find_element_by_xpath('//select[@class="ui-datepicker-year"]')
    #for option in selectYear.find_elements_by_tag_name('option'):
    #    if option.text == '2020':
    #        option.click()
    #        break
    #
    #days = driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
    #days[28].click()
    driver.find_element_by_id('JBJto_date').clear()
    driver.find_element_by_id('JBJto_date').send_keys(to_date)
    #selectMonth = driver.find_element_by_xpath('//select[@class="ui-datepicker-month"]')
    #for option in selectMonth.find_elements_by_tag_name('option'):
    #    if option.text == 'Aug':
    #        option.click()
    #        break
    #
    #selectYear = driver.find_element_by_xpath('//select[@class="ui-datepicker-year"]')
    #for option in selectYear.find_elements_by_tag_name('option'):
    #    if option.text == '2020':
    #        option.click()
    #        break
    #
    #days = driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
    #days[29].click()

    element = driver.find_element_by_id('captcha')
    location = element.location

    #print(location)

    size = element.size
    driver.save_screenshot('screenshot.png')

    captcha = driver.find_element_by_id('ansCaptcha')
    captcha.clear()

    captcha_text = get_captcha_text(location, size)
    captcha.send_keys(captcha_text)
    driver.find_element_by_id('getJBJ').click()

    time.sleep(5)

    output = driver.find_element_by_id('JBJ')

    # from bs4 import BeautifulSoup
    # page_html = driver.page_source
    # bsoup = BeautifulSoup(page_html, 'html.parser')
    source_code = output.get_attribute("outerHTML")
    print(source_code)
    #https://medium.com/@vineet_c/using-tesseract-to-solve-captcha-while-logging-in-to-a-website-with-selenium-899a810cf14


    # sql = "INSERT INTO base(frm_date, to_date, link, data) VALUES (%s, %s, %s, %s)"
    # val = ('21-03-2020','22-03-2020','https://main.sci.gov.in/judgments',source_code)
    # mycursor.execute(sql, val)

    sql = "UPDATE base SET data=%s WHERE id=%s"
    val = (source_code,str(args['id']))
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    driver.quit()
except Exception as err:
    print('ERROR: %sn' % str(err))
    mydb.close()
    driver.quit()

