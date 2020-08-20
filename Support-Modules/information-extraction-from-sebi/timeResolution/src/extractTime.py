import json
import os
import requests
file_path = './../../enitityRecognition/outputs/CoRef/'
files = os.listdir(file_path)
from tqdm import tqdm
url = "http://0.0.0.0:8000/parse"
output_file_path = "./../outputs/"
for file in tqdm(files):
  data = json.load(open(file_path + file))
  for i in (data):
    try:
      payload = dict(data='locale=en_GB', text=data[i]['text'])
      res = requests.post(url, data=payload)
      data[i]['time-raw'] = res.json()
    except:
      # print(data[i])
      data[i]['time-raw'] = []
  with open(output_file_path + file,'w') as handle:
    json.dump(data,handle)