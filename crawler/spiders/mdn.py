import json
from xml.sax.saxutils import unescape

import scrapy
from scrapy.http import JsonRequest

from crawler.items import CrawlerItem
from utils.clean_html import clean_html


class MDNSpider(scrapy.Spider):
    name = 'mdn'
    allowed_domains = ['developer.mozilla.org']
    start_urls = ['https://developer.mozilla.org/en/docs/Web/CSS/Reference']

    def parse(self, response):
        for link in response.css('div.index li a::attr(href)'):
            item_page = link.get()
            bcd_json = response.urljoin(item_page + '/bcd.json')
            yield JsonRequest(bcd_json, callback=self.parse_bcd_json)

    def parse_bcd_json(self, response):
        item = CrawlerItem()
        jsonresponse = json.loads(response.text)

        name = jsonresponse['data']['__compat']['description']
        name = clean_html(name)
        name = unescape(name)
        version = jsonresponse['data']['__compat']['support']['firefox'][-1]['version_added']
        if version:
            release_date = jsonresponse['data']['__compat']['support']['firefox'][-1]['release_date']
        else:
            release_date = None
        link = 'https://developer.mozilla.org' + jsonresponse['data']['__compat']['mdn_url']

        item['name'] = name
        item['render'] = 'firefox'
        item['version'] = version
        item['release_date'] = release_date
        item['link'] = link

        yield item
