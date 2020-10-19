import csv
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres+psycopg2://postgres:ams253526370@localhost:5432/airline"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    #SELECT * FROM flights
    flights = Flight.query.all()
    for flight in flights:
        print(flight.origin, "to", flight.destination, "takes", flight.duration, "minutes")

    #SELECT * FROM flights WHERE origin='Mexico'
    flights = Flight.query.filter_by(origin='Mexico').all()

    #SELECT * FROM flights WHERE origin != 'Mexico'
    flights = Flight.query.filter(Flight.origin != 'Mexico').all()

    #SELECT * FROM flights WHERE origin='Mexico' and duration>500
    flights = Flight.query.filter(and_(Flight.origin='Mexico',Flight.duration>500)).all()

    #SELECT * FROM flights WHERE origin='Mexico' LIMIT 1
    flights = Flight.query.filter_by(origin='Mexico').first()

    #SELECT COUNT(*) FROM flights WHERE origin='Mexico'
    flights = Flight.query.filter_by(origin='Mexico').count()

    #SELECT * FROM flights WHERE origin LIKE '%a%'
    flights = Flight.query.filter(Flight.origin.like('%a%')).all()

    #SELECT * FROM flights WHERE id=3
    flight = Flight.query.get(3)

    #UPDATE flights SET duration=150 WHERE id=3
    flight = Flight.query.get(3)
    flight.duration = 150

    db.session.commit()
    #DELETE FROM flights WHERE id=3
    flight = Flight.query.get(3)
    db.session.delete(flight)
    db.session.commit()

    #SELECT * FROM flights ORDER BY origin
    flights = Flight.query.order_by(Flight.origin).all()
    flights = Flight.query.order_by(Flight.origin.desc()).all()

    #SELECT * FROM flights JOIN passenger ON flights.id=passenger.flight_id
    db.session.query(Flight, Passenger).filter(Flight.id==Passenger.flight_id).all()

if __name__=="__main__":
    with app.app_context():
        main()
