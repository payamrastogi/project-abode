from bs4 import BeautifulSoup
import requests
import json

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}

with requests.Session() as s:
    url = 'https://www.zillow.com/homedetails/13-Cactus-Ct-Edison-NJ-08820/39070821_zpid/?utm_campaign=iosappmessage&utm_medium=referral&utm_source=txtshare'
    r = s.get(url, headers=req_headers)

soup = BeautifulSoup(r.content, 'html.parser')
#print(soup)
price = soup.findAll("span", {"data-testid": "price"})
#print(price)
#details = soup.finaAll("script",  {"id": "hdpApolloPreloadedData"})
#print(details)
details = soup.find(id="hdpApolloPreloadedData").text
d = json.loads(details)['apiCache']
d = json.loads(d)
print(d)

