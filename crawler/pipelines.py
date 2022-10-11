from datetime import datetime
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from utils.definitions import ROOT_DIR
from models.css_properties import CSSProperties
from models.release_dates import ReleaseDates


class CrawlerPipeline:
    def __init__(self):
        dist_path = os.path.join(ROOT_DIR, 'dist')
        db_path = os.path.join(dist_path, 'css_milestone.sqlite')
        engine = sqlalchemy.create_engine('sqlite:///' + db_path, echo=True)
        self.session = sessionmaker(bind=engine)()

    def process_item(self, item, spider):
        css = CSSProperties()
        css.name = item['name']
        css.render = item['render']
        css.version = item['version']
        css.link = item['link']

        css_duplicated = self.session.query(CSSProperties).\
            filter(CSSProperties.name == item['name']).\
            count() > 0
        if css_duplicated:
            return item

        self.session.add(instance=css)
        self.session.commit()

        release_duplicated = self.session.query(ReleaseDates).\
            filter(ReleaseDates.render == item['render'], ReleaseDates.version == item['version']).\
            count() > 0
        if release_duplicated:
            return item

        release = ReleaseDates()
        release.render = item['render']
        release.version = item['version']
        if item['release_date']:
            release.release_date = datetime.fromisoformat(item['release_date'])

        self.session.add(instance=release)
        self.session.commit()

        return item
