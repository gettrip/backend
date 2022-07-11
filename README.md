# Gettrip - create your unique trip

The service allows to create a trip map based on your preferences in automatic mode.
Choose a city, choose a city tour and get a map with interest points list. PDF print is awaliable.

city|tours|trip
:-:|:-:|:-:
![Alt-текст](https://github.com/gettrip/backend/blob/main/images/index.png?raw=true) | ![Alt-текст](https://github.com/gettrip/backend/blob/main/images/city_tour.png?raw=true) | ![Alt-текст](https://github.com/gettrip/backend/blob/main/images/trip.png?raw=true)

## Project structure

The service consists on two parts: backend and frontend. For running on localhost both need to be cloned:

```bash
git clone https://github.com/gettrip/backend.git
git clone https://github.com/gettrip/frontend.git
```

## Start up

### One-time action (if not poetry)

```bash
pip install poetry
poetry config virtualenvs.in-project true
source .env\Scripts\activate
```

### Install dependecies

```bash
poetry init
poetry install
```

### Configure environment

Create .env file by using .env.default.

### Create database (backend)

```bash
make db.run
make db.create
```

## Usage

```bash
make run
```

## Resources used

```bash
PostgreSQL - database management system (DBMS)
psycopg2-binary - lib. Work with PostgreSQL (multi-threaded applications)
sqlalchemy - lib. Work with different DBMS
pydantic - lib. Data validation and settings management
```
