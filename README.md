# Dronesheild-qatest


## Setup and run

Without Docker:

- Run `pip install -r requirements.txt` to install dependencies
- Run `playwright install` to install browsers
- Run with `pytest` (or with `pytest --html=reports/report.html` to generate html report)

With Docker:
- `docker build -t pytest-playwright .`
- `docker run --rm -v %cd%/reports:/app/reports pytest-playwright` (Windows)
- `docker run --rm -v $(pwd)/reports:/app/reports pytest-playwright` (Max / Linux)

## To-do

- Add linter
- Add dockerfile
- Add missing steps + features (expand test scope)
- Add details of framework