from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres+psycopg2://postgres:ams253526370@localhost:5432/airline"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    flight_id = request.form.get('flight_id')
    name = request.form.get('name')

    flight = Flight.query.get(flight_id)
    flight.add_passenger(name)

    passenger = Passenger.query.filter_by(name=name).first()

    dict = {"flight":flight, "passenger":passenger}
    return render_template("book.html", dict=dict)

@app.route("/flights")
def flights():
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight_detail(flight_id):
    flight = Flight.query.get(flight_id)
    return render_template("flight_detail.html", flight=flight)
