from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres+psycopg2://postgres:ams253526370@localhost:5432/airport")
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT * FROM flights;").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination} takes {flight.duration} minutes")

if __name__=="__main__":
    main()
