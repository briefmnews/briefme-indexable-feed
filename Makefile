clean:
	rm -rf *.egg-info .pytest_cache
	rm -rf htmlcov
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

coverage:
	pytest --cov=briefme_indexable_feed tests

report:
	pytest --cov=briefme_indexable_feed --cov-report=html tests

install:
	pip install -r requirements.txt

release:
	git tag -a $(shell python -c "from briefme_indexable_feed import __version__; print(__version__)") -m "$(m)"
	git push origin --tags
