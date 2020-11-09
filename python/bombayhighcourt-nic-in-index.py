from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint
from selenium.webdriver.support.ui import WebDriverWait
from pytesseract import image_to_string
from PIL import Image
import time
import io
import pytesseract
import pytesseract as tss
import requests
import argparse
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


def get_captcha_text(location, size):
    # pytesseract.pytesseract.tesseract_cmd = 'path/to/pytesseract'
    # tss.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    im = Image.open('screenshot.png')
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left, top, right, bottom)) # defines crop points
    im.save('screenshot.png')
    # response = requests.get("http://main.sci.gov.in/php/captcha.php")
    captcha_text = image_to_string(Image.open('screenshot.png'))
    print(captcha_text)
    print(type(captcha_text))
    return captcha_text

def get_date_select_elm(date_str='17-10-2020'):
    print("in get_date_select_elm")
    date_tds = driver.find_elements_by_css_selector("tr[bgcolor='#0099CC'] ~ tr td a")
    for date_td in date_tds :
        date_href = date_td.get_attribute("href")
        if date_href is None:
            continue
        date_href = date_href.split(".value=")[1].split(";")[0]
        #print(date_href)
        #print("'"+date_str+"'")
        if date_href == "'"+date_str+"'":
            return date_td
    return date_tds[0]


parser = argparse.ArgumentParser(description='Short sample app')
parser.add_argument('-id','--id', required=False,  type=int)

args = vars(parser.parse_args())
# print("Hi there {}, it's nice to meet you!".format(args["id"]))

try:

    frm_date = '19-10-2020'
    to_date = '22-10-2020'
    side_selected = ''
    act_selected = ''

    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    # driver.maximize_window()

    driver.get('https://bombayhighcourt.nic.in/index.html')
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    time.sleep(2)
    driver.find_element_by_link_text('Court Orders').click()

    cour_order_elm = driver.find_element_by_link_text('Court Orders')
    time.sleep(5)
    ActionChains(driver).move_to_element(cour_order_elm).perform()
    time.sleep(2)
    judgement_order_elm = driver.find_element_by_link_text('Rep. Judgment/Orders')
    ActionChains(driver).move_to_element(judgement_order_elm).perform()
    time.sleep(2)
    judgement_order_elm.click()
    side_select = Select(driver.find_element_by_css_selector('[name="m_sideflg"]'))
    side_selected = side_select.first_selected_option
    print("side selected" + side_selected.text)

    act_select = Select(driver.find_element_by_css_selector('[name="actcode"]'))
    act_selected = act_select.first_selected_option
    print("act selected" + act_selected.text)

    pick_from_to = driver.find_elements_by_css_selector("img[alt='Pick a Date']")
    print(len(pick_from_to))
    from_element = pick_from_to[0]
    to_element = pick_from_to[1]

    window_main = driver.window_handles[0]
    time.sleep(5)
    from_element.click()
    time.sleep(2)
    window_calender = driver.window_handles[1]
    driver.switch_to.window(window_calender)
    time.sleep(2)
    #date_elm = driver.find_element_by_css_selector("td[bgcolor='#FFFF33'] a")
    date_elm = get_date_select_elm(frm_date)
    href_from_date = date_elm.get_attribute("href")
    #### value of date
    href_from_date = href_from_date.split(".value=")[1].split(";")[0]
    print("selected from date"+href_from_date)
    date_elm.click()
    time.sleep(2)
    driver.switch_to.window(window_main)
    to_element.click()
    time.sleep(5)
    window_calenders = driver.window_handles
    print(len(window_calenders))
    driver.switch_to.window(window_calenders[1])
    time.sleep(5)
    #date_elm = driver.find_element_by_css_selector("td[bgcolor='#FFFF33'] + td a")
    time.sleep(2)
    date_elm = get_date_select_elm(to_date)
    href_to_date = date_elm.get_attribute("href")
    #### value of date
    href_to_date = href_to_date.split(".value=")[1].split(";")[0]
    print("selected to date"+href_from_date)
    date_elm.click()
    driver.switch_to.window(window_main)
    time.sleep(5)

    element = driver.find_element_by_id('captchaimg')
    location = element.location

    size = element.size
    driver.save_screenshot('screenshot.png')

    captcha = driver.find_element_by_id('captcha_code')
    captcha.clear()

    captcha_text = get_captcha_text(location, size)
    print(captcha_text)
    captcha.send_keys(captcha_text)
    driver.find_element_by_css_selector('[name="submit1"]').click()

    time.sleep(5)

    output = driver.find_element_by_id('JBJ')

    source_code = output.get_attribute("outerHTML")
    print(source_code)
    #https://medium.com/@vineet_c/using-tesseract-to-solve-captcha-while-logging-in-to-a-website-with-selenium-899a810cf14

    driver.quit()
except Exception as err:
    print('ERROR: %sn' % str(err))
   # mydb.close()
    driver.quit()
