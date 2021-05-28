import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def accept_all_requests():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get("https://linkedin.com")
    page_to_access = "https://www.linkedin.com/mynetwork/"
    print("Going to the Your Networks Page: ")
    driver.get(page_to_access)
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "invitation-card__action-btn")))
    finally:
        all_elements = driver.find_elements_by_class_name("invitation-card__action-btn")
        for element in all_elements:
            get_label = element.get_attribute("aria-label")
            if get_label[0: 6] == "Accept":
                print(get_label)
                element.click()
                print("The request is accepted")
    driver.close()
    return

while "1" != input("Please Enter 1 After you Have Signed In to LinkedIn: "):
    pass
accept_all_requests()
