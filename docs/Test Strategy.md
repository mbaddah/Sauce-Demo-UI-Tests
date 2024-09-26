# TEST-STRATEGY


## Objective

Capture high level testing requiremetns for e-commerce application `https://www.saucedemo.com`.

## Scope

Capture testing requirements for https://www.saucedemo.com .

Browsers
- Chrome will be default browser (explained in decisions document)

Following test phases are out of scope:
- Unit testing
- API testing
- Performance testing
- Security/Penetration testing

## Test levels/types

- Static analysis checks using `pylint`
- End to end testing using Playwright and pytest-bdd.

## Test tools and environments

- Python
- Playwright
- pytest-bdd
- Docker
- CICD using Github Actions

## Risk management

- N/A

## Test metrics & reporting

- Metrics and reports to be captured via Github actions pipeline and Playwright html report.

## Test Data Management

- Test data management details go here. Information that needs documenting includes:
    - Test data location and where data is sourced from
    - How clean up data if required
    - How to update data
    - PII considerations
    
## Entry and Exit criteria

- 'Definition of Ready' and 'Definition of Done' have been scoped out by the team (generally as part of sprint planning and backlog grooming)

## Defect management

- Generally issues will be raised in a ticket management system such as JIRA, however for the sake of this exercise, the 'Issues' functionality in Github will be used in conjuction with the 'Bug report' template and copied over to `Bugreport-1.MD`.

This covers all necessary details such as:

    - Description of the bug
    - Steps to reproduce
    - Screenshots
    - Environment details

## References

- https://pypi.org/project/pytest-bdd/
- https://playwright.dev/python/docs/intro
- 