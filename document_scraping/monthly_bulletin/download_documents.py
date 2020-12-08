import json
from os import path
import requests
from tqdm import tqdm as tqdm
import time

def process_date_for_file_name(day,ext):
    return day.replace(',','').replace(' ',"_") + ext 
with open('document_all_monthly_sebi_bulletin.json') as f:
    a = json.load(f)

for i,fc in tqdm(enumerate(a)):
    urls = fc["file_url"]
    flag = True

    file_url = urls[0]
    if file_url != None:
        file_name = file_url.split('/')[-1]
        if not path.exists(f"./collected_pdfs/{file_name}"):
            response = requests.get(file_url)
            flag = False
            with open(f"./collected_pdfs/{file_name}", "wb") as f:
                f.write(response.content)
    
    if len(urls) == 3:
        file_url = urls[1]
        file_name = process_date_for_file_name(fc["time"],".doc")
        if not path.exists(f"./collected_docx/{file_name}"):
            response = requests.get(file_url)
            flag = False
            with open(f"./collected_docx/{file_name}", "wb") as f:
                f.write(response.content)
            
        file_url = urls[2]
        file_name = process_date_for_file_name(fc["time"],".xlsx")
        if not path.exists(f"./collected_xls/{file_name}"):
            response = requests.get(file_url)
            flag = False
            with open(f"./collected_xls/{file_name}", "wb") as f:
                f.write(response.content)
    if flag == False:
        time.sleep(2)
    
