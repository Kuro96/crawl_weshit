from requests_html import HTMLSession, Element
from selenium import webdriver

class SogouWeChatCrawler:

    def __init__(self, url: str) -> None:
        self.session = HTMLSession()
        self.page = self.session.get(url)
        self.html = self.page.html
        self._block = None

    @property
    def block(self) -> Element:
        if not self._block:
            ret = self.html.xpath('//li[@id="sogou_vr_11002301_box_0"]')
            self._block = ret[0]
        return self._block

    @property
    def title(self) -> str:
        return self.block.xpath('//dl[2]/dd/a')[0].text

    @property
    def passage_url(self) -> str:
        url = self.block.xpath('//dl[2]/dd/a/@href')[0]
        if not url.startswith('https'):
            url = 'https://weixin.sogou.com' + url
        return url


if __name__ == '__main__':
    url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=%E6%AF%8F%E5%A4%A960%E7%A7%92%E8%AF%BB%E6%87%82%E4%B8%96%E7%95%8C&ie=utf8&_sug_=n&_sug_type_='
    crawler = SogouWeChatCrawler(url)
    print(crawler.title, crawler.passage_url)
    page_url = crawler.passage_url
    # driver = webdriver.Chrome()
    # pg = driver.get(page_url)

    # np = crawler.session.get(crawler.passage_url)
    import pdb; pdb.set_trace()
