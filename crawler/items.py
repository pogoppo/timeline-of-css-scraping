import scrapy


class CrawlerItem(scrapy.Item):
    name = scrapy.Field()
    render = scrapy.Field()
    version = scrapy.Field()
    release_date = scrapy.Field()
    link = scrapy.Field()
