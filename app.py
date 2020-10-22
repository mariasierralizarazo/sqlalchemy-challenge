import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to this API where you can find some of the information about Hawaii wheater <br/> "
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    latest_date = dt.datetime.strptime(latest_date[0],'%Y-%m-%d').date()
    year_ago = latest_date - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= year_ago ).order_by(Measurement.date).all()
    session.close()
    # List declaration
    all_precipitations = []

    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_precipitations.append(prcp_dict)
    return jsonify(all_precipitations)

@app.route("/api/v1.0/stations")
def stations_function():
    session = Session(engine)
    results = session.query(Measurement.station.distinct()).all()
    session.close()
    return jsonify(results)

@app.route("/api/v1.0/tobs")
def temperature():
    session = Session(engine)
    latest_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    latest_date = dt.datetime.strptime(latest_date[0],'%Y-%m-%d').date()
    year_ago = latest_date - dt.timedelta(days=365)
    active_station = session.query(Measurement.station, func.count(Measurement.station),Measurement.date).\
                    group_by(Measurement.station).filter(Measurement.date >= year_ago).\
                    order_by(func.count(Measurement.station).desc()).first()
    active_station = active_station[0]
    results = session.query(Measurement.date,Measurement.tobs).\
            filter(Measurement.date >= year_ago).\
            filter(Measurement.station == active_station).all()
    results_dict = {}
    results_dict["station"] = active_station
    results_dict["Start date"] = year_ago
    results_dict["End date"] = latest_date
    results_dict["Tobs per date"] = results
    session.close()
    return jsonify(results_dict)

if __name__ == '__main__':
    app.run(debug=True)