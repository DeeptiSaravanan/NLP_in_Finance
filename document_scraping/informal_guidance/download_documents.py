import json
from os import path
import requests
from tqdm import tqdm as tqdm
import time

def process_date_for_file_name(day,ext):
    return day.replace(',','').replace('-',"_") + ext 

with open('document_all_informal_guidelines.json') as f:
    a = json.load(f)

for i,fc in tqdm(enumerate(a)):
    urls = fc["related_docs"]
    flag = True
    if urls is not None:
        for file in urls:
            file_url = file["link"]
            file_name = process_date_for_file_name(file["date"],".pdf")

            if not path.exists(f"./collected_docs/{file_name}"):
                response = requests.get(file_url)
                flag = False
                with open(f"./collected_docs/{file_name}", "wb") as f:
                    f.write(response.content)
            else:
                "Dates repeat ??"
    if flag == False:
        time.sleep(2)
    
