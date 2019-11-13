import json # importjson library
import requests # for reading the url
from bs4 import BeautifulSoup #scrapping the data
adress1='varje,pune,india' #enter first adress
adress2='swarget,pune,india' #enter second adress
url1='http://dev.virtualearth.net/REST/V1/Routes/Driving?o=xml&wp.0={}&wp.1={}&key="Your API Key'.format(adress1,adress2) # enter your bing api key
wee=requests.get(url1) #reads the URL
soupe = BeautifulSoup(wee.content, 'html.parser') #parse the HTML file
aa=soupe.find("traveldistance") # select attribute by Given text
print(aa.get_text(),"KM") # Travelling distance between two points
