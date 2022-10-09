import os
import sqlite3

import alembic.config
from fire import Fire
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from utils.definitions import ROOT_DIR
from utils.reset_dir import reset_dir
from crawler.spiders.mdn import MDNSpider


class Commands:
    def reset(self):
        dist_path = self.dist()
        reset_dir(dist_path)

        db_path = os.path.join(dist_path, 'css_milestone.sqlite')
        sqlite3.connect(db_path).close()
        alembic.config.main(argv=['upgrade', 'head'])

    def dist(self):
        return os.path.join(ROOT_DIR, 'dist')

    def crawl(self, crawler):
        self.reset()
        process = CrawlerProcess(get_project_settings())
        process.crawl(crawler)
        process.start()


if __name__ == '__main__':
    Fire(Commands)
