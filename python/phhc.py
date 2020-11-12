rom selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import Select

try :
    driver = webdriver.Firefox(executable_path=r'C:\Users\Prabjot\Downloads\geckodriver.exe')
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://phhc.gov.in/home.php?search_param=free_text_search_judgment")
    WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
    print("#############")
    from_date = '25/10/2020'
    to_date = '26/10/2020'
    peti_name = 'aviman'
    resp_name = 'kadila'
    search_text = 'ERPF'
    case_type = 'FAO'
    case_year = '2020'
    frm_date_elm = driver.find_element_by_id('from_date')
    frm_date_elm.clear()
    frm_date_elm.send_keys(from_date)
    to_date_elm = driver.find_element_by_id('to_date')
    to_date_elm.clear()
    to_date_elm.send_keys(to_date)
    driver.find_element_by_id('pet_name').send_keys(peti_name)
    driver.find_element_by_id('res_name').send_keys(resp_name)
    driver.find_element_by_id('free_text').send_keys(search_text)
    select_caseType_elm = Select(driver.find_element_by_id('t_case_type'))
    select_caseType_elm.select_by_visible_text(case_type)
    sel_case_yr_elm = Select(driver.find_element_by_id('t_case_year'))
    sel_case_yr_elm.select_by_visible_text(case_year)
    submit_button = driver.find_element_by_css_selector('input[name="submit"]')
    time.sleep(2)
    submit_button.click()
    driver.quit()
except Exception as err:
    print('ERROR: %sn' % str(err))

    driver.quit()
