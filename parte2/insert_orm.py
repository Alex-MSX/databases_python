import csv
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres+psycopg2://postgres:ams253526370@localhost:5432/airline"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open(r"C:\Users\Carlos Ortiz\Desktop\flights.csv")
    reader = csv.reader(f)

    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)

    db.session.commit()

if __name__=="__main__":
    with app.app_context():
        main()
