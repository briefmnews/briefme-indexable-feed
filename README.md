# briefme-indexable-feed
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-270/) 
[![Django 2.x](https://img.shields.io/badge/django-2.2-blue.svg)](https://docs.djangoproject.com/en/2.2/)
![Python CI](https://github.com/briefmnews/briefme-indexable-feed/workflows/Python%20CI/badge.svg)
[![codecov](https://codecov.io/gh/briefmnews/briefme-indexable-feed/branch/main/graph/badge.svg?token=Y7O6AAJM1J)](https://codecov.io/gh/briefmnews/briefme-indexable-feed)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

Base app for indexable feed

## Installation
Install with pip:
```shell
pip install -e git://github.com/briefmnews/briefme-indexable-feed.git@master#egg=briefme_indexable_feed
```

## Setup
In order to make `briefme-indexable-feed` works, you'll need to follow the steps below.

### Settings
First you need to add `briefme_indexable_feed` to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',

    'briefme_indexable_feed',
    ...
)
```

## Tests
Testing is managed by `pytest`. Required package for testing can be installed with:
```shell
make install
``` 

To run testing locally:
```shell
pytest
``` 
