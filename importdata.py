from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
import pandas as pd



Base = declarative_base()


class DB_table(Base):
    # Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'test98'
    __table_args__ = {'sqlite_autoincrement': True}
    # tell SQLAlchemy the name of column and its attributes:
    name = Column(String(128), primary_key=True, nullable=False)
    speciality = Column(String(10))
    address = Column(String(128))
    city = Column(String(128))
    state = Column(String(10))
    zip = Column(String(5))
    lat = Column(Float)
    lng = Column(Float)


if __name__ == "__main__":

    # Create the database
    engine = create_engine("mysql+pymysql://root:qwerty1234@localhost/googlemap?charset=utf8", max_overflow=5)
    Base.metadata.create_all(engine)

    # Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()



    data = pd.read_csv('/Users/hka/Downloads/test98.csv', encoding='utf-8')
    # data = pd.read_csv('/Users/hka/Downloads/providers.csv', encoding='utf-8')
    # print(data)

    for index, row in data.iterrows():

        # print(row['name'])
        record = DB_table(**{
            'name': row['name'],
            'speciality': row['speciality'],
            'address': row['address1'],
            'city': row['city'],
            'state': row['state'],
            'zip': row['zip'],
            'lat': row['lat'],
            'lng': row['lng']
        })

        s.add(record)  # Add all the records
    s.commit()
    s.close()  # Close the connection
    print('Data Added')
