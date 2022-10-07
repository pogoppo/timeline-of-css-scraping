import scrapy


class CssSpider(scrapy.Spider):
    name = 'css'
    allowed_domains = ['developer.mozilla.org']
    start_urls = ['http://developer.mozilla.org/']

    def parse(self, response):
        pass
