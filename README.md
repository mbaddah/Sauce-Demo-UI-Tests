# Dronesheild-qatest


## Setup and run

Without Docker:

- Run `pip install -r requirements.txt` to install dependencies
- Run `playwright install` to install browsers
- Run with `pytest --html=reports/report.html` 
- To run specific tet run with `pytest -k "test_name" --html=reports/report.html`
- To run with debug mode, set environment variable `PWDEBUG=1` and run with `pytest -s`

With Docker:
- `docker build -t pytest-playwright .`
- `docker run --rm -v %cd%/reports:/app/reports pytest-playwright` (Windows)
- `docker run --rm -v $(pwd)/reports:/app/reports pytest-playwright` (Max / Linux)

## To-do

- Expand test scope
- Add details of framework
- Add hooks
- Add POM
- Screenshot on failure

## Things i would have liked to have done but didn't get time to do:

- 