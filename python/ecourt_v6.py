from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from PIL import Image
from pytesseract import image_to_string
import time
import pyautogui


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


def download_page_from_child_link():
    time.sleep(2)
    webobj = driver.find_element_by_id("download")
    webobj.click()
    #Click the OK button and close
    time.sleep(2)
    # allGUID = driver.window_handles

    # print(allGUID)
    pyautogui.press('enter')
    # time.sleep(2)
    # webobj.send_keys(Keys.RETURN)

    time.sleep(2)
    driver.close()

    #Restore the handle back to parent handle
    driver.switch_to.window(driver.window_handles[0])



# main function
if __name__ =="__main__":

    site_url = "https://services.ecourts.gov.in/ecourtindia_v6/"

    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.maximize_window()

    driver.get(site_url)
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    driver.find_element_by_id('leftPaneMenuCO').click()

    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()

        time.sleep(2)
        driver.execute_script('document.getElementById("sess_state_code").style.display = ""')
        time.sleep(2)
        Select(driver.find_element_by_id("sess_state_code")).select_by_value('13')
        time.sleep(2)
        driver.execute_script('document.getElementById("sess_dist_code").style.display = ""')
        time.sleep(2)
        Select(driver.find_element_by_id("sess_dist_code")).select_by_value('1')
        time.sleep(2)
        driver.execute_script('document.getElementById("court_complex_code").style.display = ""')
        time.sleep(2)
        Select(driver.find_element_by_id("court_complex_code")).select_by_value('101@2,3,4,5,6,7@N')
        time.sleep(2)
        driver.find_element_by_id('COorderDate').click()


        driver.find_element_by_id('from_date').send_keys('01-10-2020')

        driver.find_element_by_id('to_date').send_keys('14-10-2020')

        driver.find_element_by_id('radinterimorderdt').click()

        # driver.find_element_by_id('captcha_image')
        i = 0
        k=0
        previous = ''
        while i<20:

            captcha_text = get_captcha_image(driver)
            captcha = driver.find_element_by_id('captcha')
            captcha.clear()
            captcha.send_keys(captcha_text) #enter captcha text

            driver.execute_script('funShowRecords("CSpartyName");')

            time.sleep(3)
            try :
                WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                                            'Timed out waiting for PA creation ' +
                                                            'confirmation popup to appear.')

                alert = driver.switch_to.alert
                alert_text = alert.text
                alert.accept()

                driver.find_element_by_xpath('//a[@title="Refresh Image"]').click()

                i = i+1

            except TimeoutException:
                server_error_msg = driver.find_element_by_id('errSpan')
                if server_error_msg.is_displayed() :
                    if k == 0 :
                        driver.find_element_by_xpath('//a[@title="Refresh Image"]').click()
                        k = k+1
                        time.sleep(2)

                    i=i+1
                else :
                    break

            if previous == i :
                i=i+1
            else :
                previous = i


        output = driver.find_element_by_id('showList')
        source_code = output.get_attribute("outerHTML")

        for link in output.find_elements_by_tag_name('a') :
            link.click()

            time.sleep(2)
            driver.switch_to.window(driver.window_handles[1])
            download_page_from_child_link()

        print(source_code)
    except Exception as err:
        print('ERROR: %sn' % str(err))


