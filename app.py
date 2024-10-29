# Import dependencies
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt

# Initialize Flask app
app = Flask(__name__)

#################################################
# Database Setup
#################################################
# Create engine to connect to SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# Reflect the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Function to create a session for each route
def get_session():
    return Session(engine)

#################################################
# Flask Routes
#################################################

# Homepage route
@app.route("/")
def welcome():
    """List all available routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br/>"
    )

# Route for precipitation data
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = get_session()
    
    # Calculate the date one year ago from the last date in the dataset
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d")
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Query precipitation data for the last 12 months
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()
    session.close()

    # Convert the query results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

# Route for list of stations
@app.route("/api/v1.0/stations")
def stations():
    session = get_session()
    
    # Query all stations
    results = session.query(Station.station).all()
    session.close()

    # Convert the results into a list
    stations = [station[0] for station in results]
    return jsonify(stations)

# Route for temperature observations of the most active station
@app.route("/api/v1.0/tobs")
def tobs():
    session = get_session()
    
    # Find the most active station
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]

    # Calculate the date one year ago from the last date in the dataset
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d")
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Query temperature observations for the most active station for the past year
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= one_year_ago).all()
    session.close()

    # Convert results to a list of dictionaries
    tobs_data = [{"date": date, "temperature": tobs} for date, tobs in results]
    return jsonify(tobs_data)

# Route for temperature stats from a start date or start-end range
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature_range(start=None, end=None):
    session = get_session()
    
    # Query min, avg, and max temperatures based on start and optional end date
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    if end:
        results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    else:
        results = session.query(*sel).filter(Measurement.date >= start).all()
    
    session.close()
    
    # Format the result as a dictionary
    temp_stats = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    return jsonify(temp_stats)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
