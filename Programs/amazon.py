import requests
from bs4 import BeautifulSoup

url=" https://www.amazon.in/Faber-Castell-Tri-Click-Mechanical-Pencils-Assorted/dp/B073PT622V/?_encoding=UTF8&pd_rd_w=UHzbl&content-id=amzn1.sym.f8b2fc0c-779f-43a6-b25a-069849dd23a6%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=f8b2fc0c-779f-43a6-b25a-069849dd23a6&pf_rd_r=EDKWHV757QYS62T6DHWC&pd_rd_wg=6518r&pd_rd_r=30121643-a7c2-4bf5-b7cc-cdb7655750af&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d"

response=requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')


print (soup.prettify    )
