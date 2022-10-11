import json

import scrapy
from scrapy.http import JsonRequest

from crawler.items import CrawlerItem


class MDNSpider(scrapy.Spider):
    name = 'mdn'
    allowed_domains = ['developer.mozilla.org']
    start_urls = ['https://developer.mozilla.org/en/docs/Web/CSS/Reference']

    def parse(self, response):
        for a in response.css('div.index li a[href]'):
            name = a.css('code::text').get()
            link = a.css('::attr(href)').get()
            bcd_json = response.urljoin(link + '/bcd.json')
            yield JsonRequest(bcd_json, callback=self.parse_bcd_json, meta={'name': name})

    def parse_bcd_json(self, response):
        item = CrawlerItem()
        jsonresponse = json.loads(response.text)

        version = jsonresponse['data']['__compat']['support']['firefox'][-1]['version_added']
        if version:
            release_date = jsonresponse['data']['__compat']['support']['firefox'][-1]['release_date']
        else:
            release_date = None
        link = 'https://developer.mozilla.org' + jsonresponse['data']['__compat']['mdn_url']

        item['name'] = response.meta['name']
        item['render'] = 'firefox'
        item['version'] = version
        item['release_date'] = release_date
        item['link'] = link

        return item
