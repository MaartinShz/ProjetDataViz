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

list0=[]
for i in range(119):
 list1=list0.append(find_date('div',{'class':'fEDvV'},f"https://www.tripadvisor.fr/AttractionProductReview-g304551-d13548887-or{i}0-Same_Day_Taj_Mahal_Tour_from_Delhi-New_Delhi_National_Capital_Territory_of_De.html"))

print(list1)