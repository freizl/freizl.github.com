from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from cncrk.items import CncrkItem

class CncrkSpider(CrawlSpider):
    domain_name = "cncrk.com"
    start_urls = [
        "http://www.cncrk.com/downlist/r_1_1.html"
    ]

    #todo follow up 'next page'
    rules = [Rule(SgmlLinkExtractor(allow=['/\d+\.html']), 'parse_software')]

    def parse_software(self, response):
        hxs = HtmlXPathSelector(response)
        torrent = CncrkItem()
        torrent['url'] = response.url
        torrent['name'] = hxs.select("//div[@id='softtitle']/span/text()").extract()
        torrent['size'] = hxs.select("//div[@id='softinfo']//li[1]/text()[1]").extract()
        torrent['editor'] = hxs.select("//div[@id='softinfo']//li[9]/text()[1]").extract()
        return [torrent]

SPIDER = CncrkSpider()
