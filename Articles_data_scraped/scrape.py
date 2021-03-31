from newspaper import Article
import nltk

nltk.download('punkt')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

list_links = []
list_links1 = []
url = "https://www.mondaq.com/Home/Search?q=sebi"	
html = urlopen(url)
soup = BeautifulSoup(html)
type(soup)

all_links = soup.find_all('a',class_="gs-title")
for link in all_links:
    	list_links.append(link.get("href"))
	#list_links.append(link.a['href'])	
#for url in list_links:
#	url1 = "https://www.business-standard.com"+url
#	list_links1.append(url1)

for url in list_links:
	#print(url)
	#url= 'https://www.investopedia.com/terms/s/sebi.asp'

	article = Article(url, language="en") # en for English 

	article.download() 
	article.parse() 
	article.nlp() 

	title = article.title
	file1=open(title+".txt", "w+")
	#file1.write("Title:\n")
	file1.write(article.title)
	#file1.write("\n\nArticle Text:\n")
	file1.write("\n\n")
	file1.write(article.text)
	#file1.write("\n\nArticle Summary:\n")
	#file1.write(article.summary)
	#file1.write("\n\n\nArticle Keywords:\n")
	#keywords='\n'.join(article.keywords)
	#file1.write(keywords)
	file1.close()

#Investopedia - https://www.investopedia.com/search?q=sebi&offset=0 - 'a',class_="search-results__link mntl-text-link"

#seekingalpha - directly use article urls

#financialexpress - directly use article urls

#newshour - https://www.newshour.press/?s=sebi
	#all_links = soup.find_all('div',class_="entry-headder")
	#for link in all_links:
    	#	list_links.append(link.a['href'])

#businessstandard - https://www.business-standard.com/topic/sebi
	#all_links = soup.find_all('div',class_="listing-txt")
	#for link in all_links:
    	#	list_links.append(link.a['href'])	
	#for url in list_links:
	#	url1 = "https://www.business-standard.com"+url
	#	list_links1.append(url1)

#moneycontrol - https://www.moneycontrol.com/news/tags/sebi.html
	#all_links = soup.find_all('li',class_="clearfix")
	#for link in all_links:
		#list_links.append(link.a['href'])	
	#j=0
	#while(j<10):
		#list_links.pop(0)
		#j=j+1	

#hindubusinessline - directly use article urls

#vccircle - https://www.vccircle.com/tag/sebi/19
	#all_links = soup.find_all('div',class_="title")
	#for link in all_links:
		#list_links.append(link.a['href'])


