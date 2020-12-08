import requests
import json
from lxml import html
from tinydb import TinyDB, Query
from tqdm import tqdm as tqdm
 
db = TinyDB('db_dump.json')

with open('all_regs.json','r') as f:
    out_files = json.load(f)
    cleaned_out_files = []
    present_keys = set()
    for ele in out_files:
        if ele["url"] in present_keys:
            continue
        else:
            cleaned_out_files.append(ele)
            present_keys.add(ele["url"])
            
added_out = []

fileObj = Query()

import time
for i,file in tqdm(enumerate(cleaned_out_files)):
    time.sleep(2)
    r = requests.get(file["url"])
    tree = html.fromstring(r.content)
    
    search_obj = db.search(fileObj.url == file['url'])
    if search_obj is not None:
        if len(search_obj) != 0:
            continue
    #########################################################
    try :
        element = tree.xpath("//*[contains(@class, 'cover')]")[0].xpath("//iframe")[0]
        fc = file
        fc["file_url"] = element.attrib['src'].split("=")[1]
        added_out.append(fc)  
        db.insert(fc)
    except:
        fc = file
        fc["file_url"] = None
        db.insert(fc)  

with open('document_all_regs.json','w') as f:
    json.dump(added_out,f)