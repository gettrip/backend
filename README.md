# backend

## Install dependencies

### One-time action

```bash
pip install poetry
poetry config virtualenvs.in-project true
source .env\Scripts\activate
```

### For each projet

```bash
poetry init
poetry install
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
