import scrapy


class CrawlerItem(scrapy.Item):
    name = scrapy.Field()
    version = scrapy.Field()
