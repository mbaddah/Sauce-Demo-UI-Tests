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

You can execuete using tag annotations, e.g. `pytest -m "login and successful"` 

Headed/Headless:

- By default playwright will run in headless mode (required for CICD). To run headed, run with `--headed` option.

## Linting with `pylint`

Before raising a PR, you must run `pylint` and correct for any issues detected.

## Things i would have liked to have done but didn't get time to do:

- Expand test scope coverage
- Screenshot on failure
- Integrate with Sonarqube
- Refactor code so that credentials are read from environment variables (not hardcoded)
