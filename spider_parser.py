import re
import urllib.parse
from bs4 import BeautifulSoup
class url_parser(object):

    def _get_new_urls(self,new_url,soup):
        new_urls = set()
        links = soup.find_all('a',href = re.compile(r'/view/\d+\.htm'))
        for link in links:
            url = link['href']
            new_full_url = urllib.parse.urljoin(new_url,url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,new_url,soup):
        res_data={}
        res_data['url'] = new_url
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()
        s_node = soup.find('div',class_="lemma-summary")
        res_data['text'] = s_node.get_text()

        return res_data





    def url_parser(self,new_url,html_cout):
        if new_url is None or html_cout is None:
            return

        soup = BeautifulSoup(html_cout,'html.parser')
        new_urls = self._get_new_urls(new_url,soup)
        new_data = self._get_new_data(new_url,soup)
        return new_urls,new_data