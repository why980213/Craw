import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return
        open = urllib2.urlopen(url)
        if open.getcode() != 200:
            return
        cont = open.read()
        return cont