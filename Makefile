SHELL=bash

# Remove all python artifacts.
clean-pyc:
	@echo "Removing python artifacts..."
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
.PHONY: clean-pyc

# Run the unit tests.
unittest:
	@echo "Running unittests..."
	pytest -s -v .
	# pytest -s -v --no-print-logs .
.PHONY: unittest

# Lint python code.
lint:
	@echo "Running Python Codestyle check..."
	pycodestyle --max-line-length 100 --ignore E402,W503,W504,E704 --statistics --exclude=src/lib/* .
.PHONY: lint

# Run test coverage.
coverage:
	@echo "Run unittests and report on coverage..."
	pytest -s -v --cov-report html --cov-report term --no-cov-on-fail --cov-fail-under=35 --cov-branch --cov-config .coveragerc --cov src/
.PHONY: coverage

# Run clean-pyc, lint and unittest targets.
test: clean-pyc lint unittest
.PHONY: test

# Run clean-pyc, lint and coverage targets.
fulltest: clean-pyc lint coverage
.PHONY: fulltest
