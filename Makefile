.PHONY: format lint test sec

format:
	@isort .
	@blue .

lint:
	@blue . --check
	@isort . --check
	@prospector --with-tool pydocstyle --doc-warning

test:
	@pytest -v

sec:
	@pip-audit