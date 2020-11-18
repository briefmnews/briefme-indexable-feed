# briefme-indexable-feed
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
