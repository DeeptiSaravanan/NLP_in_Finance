#Importing packages
from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome('/home/buggi/RA/tools/chromedriver')

driver.get("https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=4&ssid=80&smid=107")

all_list = []

for i in range(12):
    print(i)
    wait = WebDriverWait(driver,10)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'pagination_outer')))    
    
    table = driver.find_elements_by_xpath("/html/body/form/div[4]/div[2]/div/section[2]/div/section/div[2]/div/div[2]/div/table/tbody/tr")
    for table_row in table:
        boxes = table_row.find_elements_by_tag_name("td")
        all_list.append({"time": boxes[0].text, 
                        "text": boxes[1].text,
                        "urls" : [ele.get_attribute("href") for ele in boxes[1].find_elements_by_tag_name("a")]
                        })

    button = driver.find_elements_by_xpath('//*[@id="ajax_cat"]/div[1]/div[2]/ul/li')
    
    WebDriverWait(driver,5)
    button[-2].click()
    # break

with open('all_monthly_sebi_bulletin.json','w') as f:
    json.dump(all_list,f)
driver.quit()
