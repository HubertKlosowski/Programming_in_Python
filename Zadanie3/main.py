import sqlalchemy as db
from sqlalchemy.exc import SQLAlchemyError

try:
    engine = db.create_engine('mysql://iris_user:iris_user@localhost:3306/flask')
    connection = engine.connect()
    metadata = db.MetaData()

    iris_data = db.Table('irisdata', metadata, autoload_with=engine)

    query = db.select(iris_data)

    result = connection.execute(query)

    for row in result.fetchall():
        print(row)

    connection.close()

except SQLAlchemyError as e:
    print(f"Error connecting to the database: {e}")
