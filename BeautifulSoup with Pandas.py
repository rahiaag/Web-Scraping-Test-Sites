import requests
import pandas as pd
from bs4 import BeautifulSoup

# A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure in pandas

url="https://www.webscraper.io/test-sites/e-commerce/allinone/phones/touch"

r=requests.get(url)

soup=BeautifulSoup(r.text,"lxml")



names=soup.find_all("a",class_="title")
#print(names)

product_name=[]

for i in names:
    name=i.text
    product_name.append(name)
#
#print(product_name)
prices=soup.find_all("h4",class_="price float-end card-title pull-right")

prices_list=[]

for i in prices:
    price=i.text
    prices_list.append(price)

#print (prices_list)

# Now we will create the data frame

df=pd.DataFrame({"Product Name": product_name,"Price" :prices_list})

print (df)

#df.to_csv("Products_Details.csv")

#df.to_excel("Products_Details Excel.csv")
