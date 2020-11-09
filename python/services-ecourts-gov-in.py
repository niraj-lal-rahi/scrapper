from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from PIL import Image
from pytesseract import image_to_string
import time

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

# main function
if __name__ =="__main__":

    site_url = "https://services.ecourts.gov.in/ecourtindia_v4_bilingual/cases/s_orderdate.php?state=D&state_cd=26&dist_cd=8"

    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.maximize_window()

    driver.get(site_url)
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    # enter static value
    courtComplex = Select(driver.find_element_by_id("court_complex_code")).select_by_value('1@1,2,3,4@N')

    fromDate = driver.find_element_by_id('from_date').send_keys('02-09-2020')
    toDate = driver.find_element_by_id('to_date').send_keys('03-09-2020')

    i = 0
    previous = ''
    while i<10:
        print(i)

        captcha_text = get_captcha_image(driver)
        captcha = driver.find_element_by_id('captcha')
        captcha.clear()
        captcha.send_keys(captcha_text) #enter captcha text

        driver.execute_script("validate();") #submit

        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                                'Timed out waiting for PA creation ' +
                                                'confirmation popup to appear.')

            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            # driver.execute_script("clearCaptchaText();") #submit
            driver.find_element_by_xpath('//a[@title="Refresh Image"]').click()
            print('alert - accept')
            print(alert_text)
            i = i+1
        except TimeoutException:

            server_error_msg = driver.find_element_by_id('errSpan')
            if server_error_msg.is_displayed() :
                i=i+1
            else :
                break


        if previous == i :
            i=i+1
        else :
            previous = i


time.sleep(10)

output = driver.find_element_by_id('showList3')
source_code = output.get_attribute("outerHTML")
print(source_code)

driver.quit()
