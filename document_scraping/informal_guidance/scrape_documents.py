import requests
import json
from lxml import html
from tinydb import TinyDB, Query
from tqdm import tqdm as tqdm

from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By

with open('all_informal_guidlines_links.json','r') as f:
    cleaned_out_files = json.load(f)
            
added_out = []
db = TinyDB('db_dump.json')
fileObj = Query()

driver = webdriver.Chrome('/home/buggi/RA/tools/chromedriver')

for i,file in tqdm(enumerate(cleaned_out_files)):

    driver.get(file["url"]) 
    wait = WebDriverWait(driver,5)    

    #########################################################
    try:
        elements = driver.find_elements_by_xpath("//*[@id='member-wrapper']/section[2]/div[1]/section/div[2]/table/tbody/tr")
        fc = file
        fc["related_docs"] = []
        for i, elem in enumerate(elements[1:]):
            tds = elem.find_elements_by_tag_name("td")
            fc["related_docs"].append({
                "date": tds[0].text,
                "text": tds[1].text,
                "link": tds[1].find_element_by_tag_name('a').get_attribute('href'),
            })

        db.insert({'num':i, 'u':fc["related_docs"]})
        added_out.append(fc)
  
    except Exception as e:
        print(e,file["url"])
        fc = file
        fc["related_docs"] = None
        added_out.append(fc)

driver.close()
with open('document_all_informal_guidelines.json','w') as f:
    json.dump(added_out,f)