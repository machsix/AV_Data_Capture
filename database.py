#%%
from sqlalchemy import create_engine, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, NCHAR
from sqlalchemy.orm import sessionmaker
import config
# import config

SQL_ENGINE = None
Base = declarative_base()
SQL_SESSION = None

class AvDB(Base):
    __tablename__ = "avdb"
    number = Column(String, primary_key=True)
    path = Column(String)

    def __repr__(self):
        return '<AvDB(number={:s} path={:s}'.format(self.number, self.path)

    @staticmethod
    def setTableName(name):
        __tablename__ = name

#%%
def connectDB():
    global SQL_ENGINE
    global SQL_SESSION
    global AvDB
    switch, url, tableName = config.getConfig().database()
    tableName = tableName.lower()
    AvDB.setTableName(tableName)
    if switch:
        SQL_ENGINE = create_engine(url, echo=False)
        SQL_SESSION = sessionmaker(bind=SQL_ENGINE)
        if not SQL_ENGINE.dialect.has_table(SQL_ENGINE, AvDB.__tablename__):
            Base.metadata.create_all(SQL_ENGINE)

#%%
def addNumber(number, path):
    global SQL_SESSION
    if SQL_SESSION is None:
        connectDB()
    ps = SQL_SESSION()
    r = True
    if ps.query(AvDB).filter(AvDB.number == number).scalar() is None:
        ps.add(AvDB(number=number, path=path))
        r = False
    ps.commit()
    ps.close()
    return r
