[![Requirements Status](https://requires.io/github/lancelote/pluralsight-unit-testing-python/requirements.svg?branch=master)](https://requires.io/github/lancelote/pluralsight-unit-testing-python/requirements/?branch=master)
[![Build Status](https://travis-ci.org/lancelote/pluralsight-unit-testing-python.svg)](https://travis-ci.org/lancelote/pluralsight-unit-testing-python)
[![Coverage Status](https://coveralls.io/repos/github/lancelote/pluralsight-unit-testing-python/badge.svg?branch=master)](https://coveralls.io/github/lancelote/pluralsight-unit-testing-python?branch=master)

# pluralsight-unit-testing-python

Code for pluralsight course [Unit Testing with Python](https://app.pluralsight.com/library/courses/unit-testing-python/table-of-contents)
by Emily Bache

## Notes

- **Stub** - returns a hard coded answer to any query (no logic)
- **Fake** - is a real implementation, yet unsuitable for production
- **Mock** - is as a Stub, but additionally verifies interactions
- **Test Spy** - lets you query afterwards to find out what happened
- **Dummy** - is for when the interface requires an argument
- **Monkeypatching** - changing code at runtime

## Progress

 - [x] Unit Testing with Python - Basic Example Using unittest
 - [x] Why and When Should You Write Unit Tests
 - [x] Using Pytest for Unit Testing in Python
 - [x] Testable Documentation with Doctest
 - [x] Test Doubles: Mocks, Fakes and Stubs
 - [x] Test Coverage and Parameterized Tests

## Unittest

```bash
python -m unittest -v
```

## Pytest

```bash
python -m pytest --doctest-modules -v
```

## Doctest

Should be in proper folder:
```bash
python -m doctest test_* -v
```

## Test Coverage

- `coverage` and `pytest-cov` packages are required
- Add `pragma: no cover` to exclude code from coverage report

### With `pytest`

Terminal report:
 ```bash
 python -m pytest --cov-report term-missing --cov <target>
 ```

HTML report:
```bash
python -m pytest --cov-report html --cov <target>
```

### With `unittest`

To generate report:
```bash
python -m coverage run -m unittest
```

To view report in terminal:
```bash
python -m coverage report
```

To view report in HTML:
```bash
python -m coverage html
```

### Coverage Branch feature

- Create `.coveragerc`
- Add - Add following code to it

```
[run]
branch=True
```
