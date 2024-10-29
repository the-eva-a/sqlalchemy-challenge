# Climate Analysis and API Project

![Climate Analysis](https://yourimageurl.com) <!-- Optional: Add an image related to the project -->

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Database Schema](#database-schema)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Setup and Database Connection](#setup-and-database-connection)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Project Overview
This project analyzes climate data in Hawaii to help plan a long vacation in Honolulu. We explore the climate dataset to understand precipitation and temperature trends, and then develop an API using Flask to serve this data. This project includes:
- Data analysis in Jupyter Notebook
- Flask-based API endpoints for accessing climate information

## Technologies Used
- Python 3.8
- SQLAlchemy
- Pandas
- Matplotlib
- Flask
- SQLite

## Database Schema
The climate database includes two main tables:
1. **Measurement**: Contains date, precipitation, temperature, and station information.
2. **Station**: Contains station details.

## Getting Started

### Installation
1. **Clone this repository**:
   ```bash
   git clone https://github.com/the-eva-a/sqlalchemy-challenge.git
   ```
2. **Navigate to the project directory:**
    ```bash
    cd sqlalchemy-challenge
    ```
### Setup and Database Connection
Ensure you have the `hawaii.sqlite` database in the `/Resources` folder. The Jupyter Notebook (`climate_starter.ipynb`) performs the data analysis, while the Flask API (app.py) connects to the database and hosts the API. 

## API Endpoints
The API provides several endpoints to access climate data:
1. **Homepage**:`/`
    Displays avalible API routes.
2. **Precipitation Data:** `/api/v1.0/precipitation`
    - Returns the last 12 months of precipitation data in JSON format.
3. **Stations**: `/api/v1.0/stations`
    - Returns a JSON list of all weather stations.
4. **Temperature Observations**: `/api/v1.0/tobs`
    - Returns temperature observations for the station with the highest activity over 
    the last 12 months. 
5. **Temperature Stats from Start Date**: `/api/v1.0/<start>`
    - Accepts a start date (`YYYY-MM-DD`) and returns minimum, average, and maximum 
    temperatures for dates after and including the starting date.
6. **Temperature Stats for a Date Range** `/api/v1.0/<start>/<end>`
    - Accepts start and end dates (`YYYY-MM-DD`) and returns minimum, average, and maximum
    temperatures for that range. 

## Usage
1. **Run the Jupyter Notebook** to explore the data:
    ``` bash
    jupyter notebook climate_starter.ipynb
    ```
2. **Start the Flask API**:
    ``` bash
    flask run
    ```
3. Access the API routes at `[http:](http://127.0.0.1:5000/)

## Example
- Access precipitation data at: `http://127.0.0.1:5000/api/v1.0/precipitation`

## Acknowledgements
This project is part of the curriculum in the edX Data Analytics Bootcamp. Special thanks to my instructors and peers for their support and guidance.

