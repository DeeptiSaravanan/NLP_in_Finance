import requests
import json
from lxml import html
from tinydb import TinyDB, Query
from tqdm import tqdm as tqdm
 
db = TinyDB('db_dump.json')

with open('all_monthly_sebi_bulletin.json','r') as f:
    cleaned_out_files = json.load(f)

from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By

added_out = []

fileObj = Query()
driver = webdriver.Chrome('/home/buggi/RA/tools/chromedriver')
import time

for i,file in tqdm(enumerate(cleaned_out_files)):
    # if len(db.search(fileObj.i == i)) == 1:
    #     continue
    driver.get(file["urls"][0]) 
    wait = WebDriverWait(driver,5)    

    #########################################################
    try:
        element = driver.find_element_by_xpath("//div[contains(@class, 'cover')]/iframe")
        fc = file
        url_string = element.get_attribute('src')
        if "=" in url_string:
            fc["file_url"] = [url_string.split("=")[1]] + fc["urls"][1:]
        else:
            fc["file_url"] = url_string.split("=") + fc["urls"][1:]
        db.insert({'num':i, 'u':fc["file_url"][0]})
        added_out.append(fc)
  
    except Exception as e:
        print(e,file["urls"][0])
        fc = file
        fc["file_url"] = [None] + fc["urls"][1:]
        added_out.append(fc)
    # break

driver.close()

with open('document_all_monthly_sebi_bulletin.json','w') as f:
    json.dump(added_out,f)


# for i,file in tqdm(enumerate(cleaned_out_files)):
#     wait = WebDriverWait(driver,2)
    
#     r = requests.get(file["urls"][0])
#     tree = html.fromstring(r.content)
#     #########################################################
#     # try :
#     if True:
#         print(r.content)
#         element = tree.xpath("//div[contains(@class, 'cover')]")
#         print(element)
#         # print(html.tostring(element))
#         fc = file
#         fc["file_url"] = [element.attrib['src'].split("=")[1]] + fc["urls"][1:]

#         added_out.append(fc)  
#     # except Exception as e:
#     #     print(e)
#     #     fc = file
#     #     fc["file_url"] = [None] + fc["urls"][1:]
#     #     added_out.append(fc)
#     break