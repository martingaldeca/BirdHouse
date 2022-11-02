from datetime import datetime
from sqlalchemy import (
    create_engine, Column, Integer, String, DateTime,
    ForeignKey, event, Boolean,
)
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation
from sqlalchemy.ext.declarative import declarative_base

import settings

engine = create_engine('sqlite:///database/birdHouse.db')
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)


def init_db():
    Model.metadata.create_all(bind=engine)


Model = declarative_base(name='Model')
Model.query = db_session.query_property()


class Sighting(Model):
    __tablename__ = 'sighting'
    id = Column(Integer(), primary_key=True)
    date = Column(DateTime(), default=datetime.now())
    message_send = Column(Boolean(), default=True)

    def __str(self):
        return f'{self.id} - {self.date} - {self.message_send}'

    @property
    def recently_sighting(self):
        if settings.RECENTLY_SIGHTING < (datetime.now() - self.date).total_seconds():
            return False
        return True
