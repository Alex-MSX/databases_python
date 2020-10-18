from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgres+psycopg2://postgres:ams253526370@localhost:5432/airport")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    flight_id = request.form.get('flight_id')
    name = request.form.get('name')

    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
    {"name":name, "flight_id":flight_id})

    db.commit()

    dict = {"flight_id":flight_id, "name":name}
    return render_template("book.html", dict=dict)

@app.route("/flights")
def flights():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight_detail(flight_id):
    flight = db.execute("SELECT * FROM flights WHERE flight_id=:flight_id",{"flight_id":flight_id}).fetchone()
    passengers = db.execute("SELECT * FROM passengers WHERE flight_id=:flight_id", {"flight_id":flight_id}).fetchall()
    dict = {"flight":flight, "passengers":passengers}
    return render_template("flight_detail.html", dict=dict)
