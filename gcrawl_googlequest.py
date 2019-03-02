import requests
import time
from bs4 import BeautifulSoup
import json
import pprint

pp = pprint.PrettyPrinter(indent=2)

class RequestGoogle:
    def __init__(self):
        self.session = requests.Session()
        ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        self.headers = {'User-Agent': ua, 'Referer':'https://www.google.com'}

    def request_list(self, keyword_list, proxified_ssh=''):
        result = []

        for index, keyword in enumerate(keyword_list):
            if proxified_ssh:
                proxy = 'socks5://127.0.0.1:{}'.format(proxified_ssh)
                search_url = "https://www.google.com/search?q={}&source=lnms&tbm=isch&safe=active" # SafeSearch : on
                rq = self.session.get(search_url.format(keyword), headers=self.headers, proxies = {'http': proxy,'https': proxy})
            else:
                rq = self.session.get(search_url.format(keyword), headers=self.headers)
            if rq.status_code==200:
                print('Got the page, scraping links, keyword {} of {}.............'.format(index+1, len(keyword_list)))
                soup = BeautifulSoup(rq.text, 'lxml')
                img_metadata_raw = [x.get_text() for x in soup.find_all('div', class_='rg_meta notranslate')]
                # normal_search = self.get_search_snippet(keyword, proxified_ssh)
                if len(img_metadata_raw) < 10:
                    print ('Result doesn\'t seem right, I\'m quitting')
                    continue
                else:
                    entry = {}
                    entry['keyword'] = keyword
                    entry['keyword_title'] = keyword.title()
                    # entry['snippet'] = normal_search
                    entry['metadata'] = [json.loads(x) for x in img_metadata_raw]
                    result.append(entry)
                    # pp.pprint(entry)
                    print('_____________________\nGoogling done, Keyword: {}, Total: {}\n_____________________'.format(keyword, len(img_metadata_raw)))
                time.sleep(1)
            else:
                print ('DID NOT got the page, result = {}'.format(rq))
        return result

    # def get_search_snippet(self, keyword, proxified_ssh=''):
    #     if proxified_ssh:
    #         proxy = 'socks5://127.0.0.1:{}'.format(proxified_ssh)
    #         search_url = "https://www.google.com/search?q={}&source=lnms&safe=active" # SafeSearch : on
    #         rq = self.session.get(search_url.format(keyword), headers=self.headers, proxies = {'http': proxy,'https': proxy})
    #     else:
    #         rq = self.session.get(search_url.format(keyword), headers=self.headers)

    #     if rq.status_code==200:
    #         soup = BeautifulSoup(rq.text, 'lxml')
    #         result = {'snippet':'', 'source': ''}
    #         for entry in soup.find_all('div', class_='g'):
    #             if entry.find('div', class_='s'):
    #                 current_source = entry.find('div', class_='r').find('a')['href']
    #                 current_snippet = entry.find('div', class_='s').find('span', class_='st').get_text()
    #                 if len(current_snippet) > len(result['snippet']):
    #                     result['snippet'] = current_snippet
    #                     result['source'] = current_source

    #         print ('RESULTTTTTTT : {}\n_____________________'.format((result)))
    #         return result
    #     else:
    #         print ('DID NOT got the page, result = {}\n{}\n^^^^^^^^^^'.format(rq, rq.text))
    #         return {}

# c = RequestGoogle().request_list(['go girl'], proxified_ssh='9001')
# print (c)