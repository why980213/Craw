# coding: utf8
import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.url = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.url.add_new_url(root_url)
        while self.url.has_new_url():
            new_url = self.url.get_new_url()
            cont = self.downloader.download(new_url)
            new_urls, new_data = self.parser.parse(new_url, cont)
            self.url.add_new_urls(new_urls)
            self.outputer.collect(new_data)
            count += 1
            if count == 10:
                break
        self.outputer.output()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/link?url=_tajZbV15LrfCA3sM_KZM7lHcVCg0_3P44hJJCyHPinEKj-WdLqi_mMov8ksd6Fn5pJ0XZBBnXEeuopKo8mpB_"
    spider = SpiderMain()
    spider.craw(root_url)



