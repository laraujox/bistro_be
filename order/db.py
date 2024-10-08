from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///orders.db', echo=True)

# Configured a scoped session (which acts similarly to Django's ORM objects manager)
Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

Base.query = Session.query_property()
