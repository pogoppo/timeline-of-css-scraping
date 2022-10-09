from datetime import datetime
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from utils.definitions import ROOT_DIR
from models.css_properties import CSSProperties


class CrawlerPipeline:
    def __init__(self):
        dist_path = os.path.join(ROOT_DIR, 'dist')
        db_path = os.path.join(dist_path, 'css_milestone.sqlite')
        engine = sqlalchemy.create_engine('sqlite:///' + db_path, echo=True)
        self.session = sessionmaker(bind=engine)()

    def __del__(self):
        self.session.close()

    def process_item(self, item, spider):
        css = CSSProperties()
        css.name = item['name']
        css.render = item['render']
        css.version = item['version']
        css.link = item['link']
        css.created_at = datetime.now()

        self.session.add(instance=css)
        self.session.commit()

        return item
