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

sqlSelect = "SELECT * FROM delhi_high_court_cases WHERE id="+str(args['id'])
mycursor.execute(sqlSelect)

myresult = mycursor.fetchone()
print(myresult)
# for x in myresult:
#mydb.close()
caseType = myresult[2]
cno = myresult[3]
year = myresult[4]
# print("%s",myresult[1])
try:
    #options = FirefoxOptions()
    #options.add_argument("--headless")

    #driver = webdriver.Firefox(options=options)
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    # driver.maximize_window()

    driver.get('http://delhihighcourt.nic.in/case.asp')
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    time.sleep(2)


    caseField = Select(driver.find_element_by_xpath("//select[@name='ctype_29']"))
    #caseField = driver.find_element_by_xpath("//form[@name='case_status']//select[@name='ctype_29']")
    caseField.select_by_value(caseType)

    case_noField = driver.find_element_by_xpath("//input[@name='cno']").send_keys(cno)

    yearField = Select(driver.find_element_by_xpath("//select[@name='cyear']"))
    yearField.select_by_value(year)

    captcha = driver.find_element_by_id("hiddeninputdigit").get_property("value")

    #insert captch
    driver.find_element_by_id("inputdigit").send_keys(captcha)

    driver.find_element_by_xpath("//form[@name='case_status']").submit()

    time.sleep(4)

    output = driver.find_element_by_id('InnerPageContent')
    source_code = output.get_attribute("outerHTML")


    sql = "UPDATE delhi_high_court_cases SET data=%s WHERE id=%s"
    val = (source_code,str(args['id']))
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    driver.quit()
except Exception as err:
    print('ERROR: %sn' % str(err))
    mydb.close()
    driver.quit()

