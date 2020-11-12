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
import mysql.connector

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

        stateSelect  = driver.find_element_by_id('sess_state_code')
        stateOptions = [x for x in stateSelect.find_elements_by_tag_name("option")]


        data = []

        config = {
            'user': 'root',
                'password': 'root',
                    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
                        'database': 'scrapper',
                            'raise_on_warnings': True,
        }

        mydb = mysql.connector.connect(**config)



        currentState = "19"
        start = False
        for element in stateOptions:
            # data.append(["name" => element.text, "value" => element.get_attribute("value")]
            stateValue = element.get_attribute("value")

            if start :
                currentState = stateValue

            if element.text != "Select State" :

                if currentState == stateValue :

                    start  = True


                    mycursor = mydb.cursor()
                    sql = "INSERT INTO ecourt_states(id, name) VALUES (%s,%s)"
                    val = (stateValue,element.text)
                    mycursor.execute(sql, val)
                    mydb.commit()

                    print( "State===> %s" %str(stateValue))

                    Select(driver.find_element_by_id("sess_state_code")).select_by_value(stateValue)

                    time.sleep(2)
                    driver.execute_script('document.getElementById("sess_dist_code").style.display = ""')

                    time.sleep(1)

                    districtSelect = driver.find_element_by_id('sess_dist_code')
                    districtOptions = [x for x in districtSelect.find_elements_by_tag_name("option")]

                    for distelement in districtOptions:
                        districtValue = distelement.get_attribute("value")
                        if distelement.text != "Select District" :

                            print( "district===> %s" %str(districtValue))
                            # insert in distict court
                            mycursor = mydb.cursor()
                            sql = "INSERT INTO ecourt_districts(value, name,ecourt_states_id) VALUES (%s,%s,%s)"
                            val = (districtValue,distelement.text,stateValue)
                            mycursor.execute(sql, val)
                            mydb.commit()

                            districtInsertId = mycursor.lastrowid

                            Select(driver.find_element_by_id("sess_dist_code")).select_by_value(districtValue)
                            time.sleep(2)

                            driver.execute_script('document.getElementById("court_complex_code").style.display = ""')
                            time.sleep(1)

                            courtComplex = driver.find_element_by_id('court_complex_code')

                            courtComplexOptions = [x for x in courtComplex.find_elements_by_tag_name("option")]

                            for courtCompelx in courtComplexOptions:

                                courtCompelxValue = courtCompelx.get_attribute("value")
                                if courtCompelx.text != "Select Court Complex" :
                                    print( "court Complex for %s " %str(courtCompelxValue) )
                                    # insert in court complex court
                                    mycursor = mydb.cursor()
                                    sql = "INSERT INTO ecourt_court_complexes(value, name,ecourt_districts_id) VALUES (%s,%s,%s)"
                                    val = (courtCompelxValue,courtCompelx.text,districtInsertId)
                                    mycursor.execute(sql, val)
                                    mydb.commit()



        mydb.close()




    except Exception as err:
        print('ERROR: %sn' % str(err))
        driver.quit()
        mydb.close()
