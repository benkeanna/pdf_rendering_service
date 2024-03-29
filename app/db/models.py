import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime

from app import db
from utils.document import STATUS_PROCESSING, STATUS_DONE


class Document(db.Model):
    __tablename__ = 'document'
    id = Column(String(50), primary_key=True)
    status = Column(Enum(STATUS_PROCESSING, STATUS_DONE, name='status_enum'), nullable=False)
    filepath = Column(String(255), unique=True, nullable=False)
    num_of_pages = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, id=None, status=None, filepath=None, num_of_pages=None):
        self.id = id
        self.status = status
        self.filepath = filepath
        self.num_of_pages = num_of_pages

    def __repr__(self):
        return f'<Document {self.id!r}>'

    @property
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Page(db.Model):
    __tablename__ = 'document_page'
    id = Column(Integer, primary_key=True)
    document_id = Column(String(50), ForeignKey('document.id'), nullable=False)
    filepath = Column(String(255), unique=True, nullable=False)
    page_number = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    modified_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, document_id=None, filepath=None, page_number=None):
        self.document_id = document_id
        self.filepath = filepath
        self.page_number = page_number

    def __repr__(self):
        return f'<Page {self.id!r}>'

    @property
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
