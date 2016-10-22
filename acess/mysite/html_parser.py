# coding utf8

from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        list = {}
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('h1')
        list['title'] = title_node.get_text()

        summary_node = soup.find('title')
        list['summary'] = summary_node.get_text()

        return list

    def parse(self, url, cont):
        if url is None or cont is None:
            return

        soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8' )
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data
