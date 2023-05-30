import json
import requests
from bs4 import BeautifulSoup

link = 'https://www.zillow.com/homedetails/5958-SW-4th-St-Miami-FL-33144/43835884_zpid/'

d = ""


def fetch_content(link, verbose=False):
    content = requests.get(link, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(content.text, "html.parser")
    item = soup.select_one("script#hdpApolloPreloadedData").text
    d = json.loads(item)['apiCache']
    d = json.loads(d)
    if verbose:
        print(d)
    return d


def process_fetched_content(raw_dictionary=None):
    if raw_dictionary is not None:
        keys = [k for k in raw_dictionary.keys() if k.startswith('VariantQuery{"zpid":')]
        results = dict((k.split(':')[-1].replace('}', ''), d.get(k).get('property', None)) for k in keys)
        return results
    else:
        return None


results = process_fetched_content(raw_dictionary=fetch_content(link, verbose=False))
print(results)
