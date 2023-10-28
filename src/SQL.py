from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:root123!@hostname:3306/testdb", echo=True)

