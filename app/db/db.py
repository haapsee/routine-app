from sqlalchemy import create_engine

def getEngine():
    engine = create_engine('sqlite:///app.db', echo=True)
    return engine


