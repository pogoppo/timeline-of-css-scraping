from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

ReleaseDatesBase = declarative_base()


class ReleaseDates(ReleaseDatesBase):
    __tablename__ = 'release_dates'

    render = Column(String, primary_key=True)
    version = Column(Integer, primary_key=True)
    release_date = Column(DateTime, nullable=True)
