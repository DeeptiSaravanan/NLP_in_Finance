import json
with open("db_dump.json",'r') as f:
    a = json.load(f)
from os import path
import requests
from tqdm import tqdm as tqdm
import time
for id in tqdm(a["_default"]):
    # print(a["_default"][id])
    file_url = a["_default"][id]['file_url']
    if file_url != None:
        file_name = a["_default"][id]['file_url'].split('/')[-1]
        if path.exists(f"./collected_docs/{file_name}"):
            print("Exists")
            continue
        response = requests.get(file_url)
        with open(f"./collected_docs/{file_name}", "wb") as f:
            f.write(response.content)
        time.sleep(2)