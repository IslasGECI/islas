.PHONY: tests

tests:
	pytest --cov=islas --cov-report=term --verbose
