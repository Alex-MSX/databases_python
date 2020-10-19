import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres+psycopg2://postgres:ams253526370@localhost:5432/airport")
db = scoped_session(sessionmaker(bind=engine))

def main():
    ruta = os.path.join(os.path.join(os.path.join(os.path.join(os.environ['USERPROFILE'])),'Desktop'),'flights.csv')
    f = open(ruta)
    reader = csv.reader(f)

    for o, dest, dur in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
        {"origin":o, "destination":dest, "duration":dur})

        print("Registro agregado:", o, dest, dur)
    db.commit()

if __name__=="__main__":
    main()
