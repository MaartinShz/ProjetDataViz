# -*- coding: utf-8 -*-
from encodings.utf_8 import encode
from bs4 import BeautifulSoup
import requests

def find_date(tag, classe, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    arr = []
    if tag == 'div':
        for t_tag in soup.find_all(tag, classe):
            arr.append(t_tag.text)
    return arr

list =find_date('div',{'class':'fEDvV'},"https://www.tripadvisor.fr/Attraction_Review-g297683-d317329-Reviews-Taj_Mahal-Agra_Agra_District_Uttar_Pradesh.html")
print(list)
