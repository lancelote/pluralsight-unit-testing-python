# pluralsight-unit-testing-python

Code for pluralsight course [Unit Testing with Python](https://app.pluralsight.com/library/courses/unit-testing-python/table-of-contents)
by Emily Bache

## Notes

- **Stub** - returns a hard coded answer to any query (no logic)
- **Fake** - is a real implementation, yet unsuitable for production
- **Mock** - is as a Stub, but additionally verifies interactions
- **Test Spy** - lets you query afterwards to find out what happened
- **Dummy** - is for when the interface requires an argument

## Progress

 - [x] Unit Testing with Python - Basic Example Using unittest
 - [x] Why and When Should You Write Unit Tests
 - [x] Using Pytest for Unit Testing in Python
 - [x] Testable Documentation with Doctest
 - [ ] Test Doubles: Mocks, Fakes and Stubs
 - [ ] Test Coverage and Parameterized Tests

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
