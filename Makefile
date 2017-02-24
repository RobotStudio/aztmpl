DOC_DIR = docs

.PHONY: init test docs

init:
	pip install -r requirements.txt

test:
	tox

coverage:
	pytest --cov=sample tests

docs:
	$(MAKE) -C $(DOC_DIR) html

pep8-verbose:
	pep8 --show-source --show-pep8 sample

pep8:
	pep8 --statistics -qq sample

autopep8:
	autopep8 -r -aa .

devreqs:
	pip-compile --output-file dev-requirements.txt dev-requirements.in

prodreqs:
	pip-compile --output-file requirements.txt requirements.in

