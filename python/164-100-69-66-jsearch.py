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

sqlSelect = "SELECT date FROM j_searches WHERE id="+str(args['id'])
mycursor.execute(sqlSelect)

myresult = mycursor.fetchone()

date = myresult[0]
try:
    options = FirefoxOptions()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    # driver.maximize_window()

    driver.get('http://164.100.69.66/jsearch/')
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    time.sleep(3)

    driver.find_element_by_xpath("//input[@name='Submit3']").click()

    driver.switch_to.frame("dynfr")

    driver.execute_script("document.getElementById('juddt').removeAttribute('readonly');")


    driver.find_element_by_id('juddt').clear()
    driver.find_element_by_id('juddt').send_keys(date)


    driver.find_element_by_id('Submit').click()

    all_tables = driver.find_element_by_xpath('//body/table[2]')
    output = all_tables.get_attribute("outerHTML")
    print(output)

    sql = "UPDATE j_searches SET data=%s WHERE id=%s"
    val = (output,str(args['id']))
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    driver.quit()
except Exception as err:
    print('ERROR: %sn' % str(err))
    mydb.close()
    driver.quit()







