import requests
from bs4 import BeautifulSoup

class CovidScraper:

    def get_url_to_scrape(url):
        print('hello soup')
        # url = 'https://www.worldometers.info/coronavirus/'
        # try:
        #     get_request = requests.get(url)
        #     data_parsed =  get_request.text
        #     souped_data = BeautifulSoup(data_parsed)
        #     print(souped_data.title.text)
        # except Exception:
        #     pass


