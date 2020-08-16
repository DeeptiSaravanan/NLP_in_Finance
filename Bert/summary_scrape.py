import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
list_links = []
list_links1 = []
url = "http://indiabusinessinsight.com/ibi/searchResult/?q=%26quot%3Bsecurities+and+exchange+board+of+india+%28sebi%29%26quot%3B&mq=+%22securities+and+exchange+board+of+india+%28sebi%29%22&fa=industry_category%2Cbusiness_term%2Ccompany_name%2Cproduct_name%2Csource_name%2Cpublication_year%2Cpublication_date%2Cstatus&s=-score"	
html = urlopen(url)
soup = BeautifulSoup(html)
type(soup)

Topic = []
Summary = []
c1 = []
c2 = []

all_links = soup.find_all('li',class_="result")
for link in all_links:
	print("links: ")
	print(link)
	l = link.find('div',class_="field article_name")
	c1 = c1.append(l.find('p').text)

print(c1)	

authorlink = soup.find_all('div', class_="abstract_text")
for link1 in authorlink:
	c2.append(link1.get_text())

Topic.append(c2)
Summary.append(c1)
dict = {'Topic' : Topic[0], 'Summary' : Summary[0]}
df = pd.DataFrame(dict)
print(df)
'''

import re
import requests

link = 'http://indiabusinessinsight.com/ibi/searchResult/?q=%26quot%3Bsecurities+and+exchange+board+of+india+%28sebi%29%26quot%3B&mq=+%22securities+and+exchange+board+of+india+%28sebi%29%22&fa=industry_category%2Cbusiness_term%2Ccompany_name%2Cproduct_name%2Csource_name%2Cpublication_year%2Cpublication_date%2Cstatus&s=-score'

r = requests.get(link)
soup = BeautifulSoup(r.text, "html.parser")

for i in soup.find_all('div', {'class': "web interface download_icon_img"}):
    print(re.search('http://', i.get('href')).group(0))	

