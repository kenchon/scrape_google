import json
from urllib import parse
import requests
from bs4 import BeautifulSoup
import argparse

# argparser settings
parser = argparse.ArgumentParser(description='Args')
parser.add_argument('--keyword', dest='keyword', type=str, default="Google",
                    help='keyword to be searched')
parser.add_argument('--ctype', dest='ctype', type=str, default="text",
                    help='type of the contents, {text, image}')
parser.add_argument('--cnum', dest='cnum', type=int, default=100,
                    help='number of the contents')   

# Scraping functions
class Scraper:
    def __init__(self):
        self.GOOGLE_SEARCH_URL = 'https://www.google.co.jp/search'
        self.session = requests.session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'})

    def Search(self, keyword, ctype='text', maximum=50):
        print('Google', ctype.capitalize(), 'Search :', keyword)
        result_json = {'keyword':keyword, 'ctype':ctype,}
        result, total = [], 0
        query = self.query_gen(keyword, ctype)
        while True:
            # get raw html
            html = self.session.get(next(query)).text
            links = self.get_links(html, ctype)

            # collect scraping results
            if not len(links):
                print('-> No more links')
                break
            elif len(links) > maximum - total:
                result += links[:maximum - total]
                break
            else:
                result += links
                total += len(links)

        print('-> Finally got', str(len(result)), 'links')
        return result

    def query_gen(self, keyword, ctype):
        # query generator
        page = 0
        while True:
            if ctype == 'text':
                params = parse.urlencode({
                    'q': keyword,
                    'num': '100',
                    'filter': '0',
                    'start': str(page * 100)})
            elif ctype == 'image':
                params = parse.urlencode({
                    'q': keyword,
                    'tbm': 'isch',
                    'filter': '0',
                    'ijn': str(page)})

            yield self.GOOGLE_SEARCH_URL + '?' + params
            page += 1

    def get_links(self, html, ctype):
        """
        
        """
        soup = BeautifulSoup(html, 'lxml')
        if ctype == 'text':
            elements = soup.select('.rc > .r > a')
            links = [e['href'] for e in elements]
        elif ctype == 'image':
            elements = soup.select('.rg_meta.notranslate')
            jsons = [json.loads(e.get_text()) for e in elements]
            links = [js['ou'] for js in jsons]
        return links
    
if __name__ == "__main__":
    args = parser.parse_args()
    g = Scraper()
    res = g.Search(keyword=args.keyword, ctype=args.ctype, maximum=args.cnum)
    for i in res: print(i)