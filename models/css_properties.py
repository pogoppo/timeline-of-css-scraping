from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

CSSPropertiesBase = declarative_base()


class CSSProperties(CSSPropertiesBase):
    __tablename__ = 'css_properties'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    render = Column(String, nullable=False)
    version = Column(Integer, nullable=False)
    link = Column(String)
    note = Column(String)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
