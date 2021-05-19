#Simple assignment
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def open_app(pincode):
    driver = Chrome()
    driver.get("https://selfregistration.cowin.gov.in/")
    mobile_no = driver.find_element(By.ID, "mat-input-0").send_keys("9551045397" + Keys.ENTER)
    otp_btn = driver.find_element_by_tag_name('ion-button').click()
    # sleep(2)
    # driver.find_element_by_tag_name('input').click()  #click on otp field and be ready
    set_search(driver,pincode)
    filter_by_pincode(driver,pincode)
    # filter_by_district(driver)
    return True

# authenticated = False

# while (not authenticated):
#     otp = input("Enter the otp: ")
#     otp_no = driver.find_element_by_tag_name('input').send_keys(str(otp) + Keys.ENTER)
#     otp_verify_btn = driver.find_element_by_tag_name('ion-button').click()
#     sleep(1)
#     if driver.current_url == "https://selfregistration.cowin.gov.in/":
#         print("Check Otp")
#     else:
#         authenticated = True
#         break

# sleep(2)

# otp = input("proceed?")

# links = driver.find_elements_by_tag_name('a')

#Roshan link id 5
#schedule for roshan
# links[5].click()
#dad link id 7

# links[7].click()

def set_search(driver,pincode):
    next_step = False
    while (not next_step):
        if driver.current_url == "https://selfregistration.cowin.gov.in/appointment":
            next_step = True
        else:
            print("waiting")
            print(pincode)
            

def filter_by_pincode(driver,pincode):
    driver.find_element_by_xpath("//input[@type='search']").send_keys(str(pincode) + Keys.ENTER)
    # ## submit
    driver.find_element_by_tag_name('ion-button').click()

def filter_by_district(driver):
    driver.find_element_by_class_name("custom-checkbox").click()
    sleep(0.1)
    ## select state
    driver.find_elements_by_tag_name("mat-select")[0].click()
    states = driver.find_elements_by_tag_name("mat-option")
    for state in states:
        if state.get_attribute('innerHTML').find("Tamil Nadu") > 0:
            state_id=state.get_attribute('id')

    driver.find_element(By.ID, state_id).click()

    sleep(0.2)

    ## select district
    driver.find_elements_by_tag_name("mat-select")[1].click()
    states = driver.find_elements_by_tag_name("mat-option")
    for state in states:
        if state.get_attribute('innerHTML').find("Chennai") > 0:
            state_id=state.get_attribute('id')

    driver.find_element(By.ID, state_id).click()

    ## submit
    driver.find_element_by_tag_name('ion-button').click()
    sleep(0.2)



def filter_by_age(driver):
    ## apply filters
    filter_list = driver.find_elements_by_class_name("form-check")
    for attri in filter_list:
        if attri.get_attribute('innerHTML').find("Age 18+") > 0:
            attri.click()
        if attri.get_attribute('innerHTML').find("Covaxin") > 0:
            attri.click()


def main(pincode):
    print("pincode is")
    print(pincode)
    open_app(pincode)
    input("proceed?")