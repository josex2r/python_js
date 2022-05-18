# python_js

`python_js` is a simple Python module which ports some JS functions to Python.

This is not production safe and it's made for learning purposes. I know this is not Pythonic's stylish but it's just a playground to learn some basics about this language.

## Features

- Some array methods
- Type checking
- Linter
- Local publishing using `Pypi` test environment.
- Automatic publish using `Github Actions` + `semantic-release`
- Local & CI testing using `tox`

## Requirements

- `python >= 3.10` 
- `pipenv`

## Install

```bash
pipenv install
```

## Running linters

```bash
pipenv run lint
```

## Running tests

Run all tests using `tox`:

```bash
tox
```

Using the current python version:

```bash
pipenv run test
```

## Publish

Test `Pypi` from local:

```bash
pipenv run publish_raw
```
