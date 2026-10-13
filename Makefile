.PHONY: dev test lint fmt check registry docs docs-dev clean

VENV   := .venv
PYTHON := $(VENV)/bin/python
PIP    := $(VENV)/bin/pip
BUNDLES := $(patsubst %/bundle.toml,%,$(wildcard */bundle.toml))

$(VENV)/bin/activate:
	python3 -m venv $(VENV)

## Install the tools in editable mode with dev extras
dev: $(VENV)/bin/activate
	$(PIP) install -e ".[dev]"

## Run the tool tests
test: dev
	$(VENV)/bin/pytest

## Check linting and formatting of the tools (no fixes)
lint: dev
	$(VENV)/bin/ruff check .
	$(VENV)/bin/ruff format --check .

## Auto-fix lint issues and apply formatting
fmt: dev
	$(VENV)/bin/ruff check --fix .
	$(VENV)/bin/ruff format .

## OKF lint of every bundle, and the generated bundle registry in sync
check: dev
	@for b in $(BUNDLES); do echo "== $$b"; $(PYTHON) tools/lint_okf.py $$b/wiki || exit 1; done
	$(PYTHON) tools/bundles.py --check

## Regenerate the bundle tables of README.md and of the consultation skill
registry: dev
	$(PYTHON) tools/bundles.py --write

## Build the documentation site into docs/.vitepress/dist
docs: dev
	cd docs && npm install && PATH="$(CURDIR)/$(VENV)/bin:$$PATH" npm run docs:build

## Serve the documentation site with live reload
docs-dev: dev
	cd docs && npm install && PATH="$(CURDIR)/$(VENV)/bin:$$PATH" npm run docs:dev

## Remove build artifacts
clean:
	rm -rf dist/ build/ *.egg-info tools/*.egg-info .pytest_cache .ruff_cache .coverage coverage.xml
	rm -rf docs/.vitepress/dist docs/.vitepress/cache docs/.vitepress/generated docs/public/data docs/public/bundles
	find docs/bundles -mindepth 1 -maxdepth 1 -type d -exec rm -rf {} +
	find . -type d -name __pycache__ -not -path "./docs/node_modules/*" -exec rm -rf {} + 2>/dev/null; true
