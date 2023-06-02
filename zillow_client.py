from bs4 import BeautifulSoup
import requests
import json


class ZillowClient:
    def __init__(self):
        pass

    @staticmethod
    def fetch(url):
        req_headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.8',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
        }
        raw_dict = {}
        try:
            with requests.Session() as s:
                r = s.get(url, headers=req_headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            details = soup.find(id="hdpApolloPreloadedData").text
            raw_dict = json.loads(details)['apiCache']
            raw_dict = json.loads(raw_dict)
        except Exception as e:
            print(e)
        return raw_dict

    @staticmethod
    def process_fetched_content(raw_dictionary=None):
        new_dict = {}
        if raw_dictionary is not None:
            for k in raw_dictionary.keys():
                # Add property details
                if k.startswith('VariantQuery{"zpid":'):
                    property = raw_dictionary.get(k).get('property', None)
                    # print(property)
                    new_dict.update(property)
                # get zestimate, bedrooms, bathrooms, yearBuilt, etc.
                if k.startswith('ForSaleShopperPlatformFullRenderQuery{"zpid"'):
                    property = raw_dictionary.get(k).get('property', None)
                    new_dict['zestimate'] = property['zestimate']
                    new_dict['bedrooms'] = property['bedrooms']
                    new_dict['bathrooms'] = property['bathrooms']
                    new_dict['yearBuilt'] = property['yearBuilt']
                    new_dict['comps'] = property['comps']
                    new_dict['taxHistory'] = property['taxHistory']
                    new_dict['priceHistory'] = property['priceHistory']
                    new_dict['description'] = property['description']
        return new_dict


if __name__ == "__main__":
    zillow_client = ZillowClient()
    # Quick Test
    raw = zillow_client.fetch(
        "https://www.zillow.com/homedetails/3-Prusakowski-Blvd-Parlin-NJ-08859/64487996_zpid/?utm_campaign=iosappmessage&utm_medium=referral&utm_source=txtshare")
    processed = zillow_client.process_fetched_content(raw)
    print(processed)
