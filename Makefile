.DEFAULT_GOAL:=help
.ONESHELL:
ENV_PREFIX=$(shell python3 -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")
USING_PDM=$(shell python3 -c "if __import__('pathlib').Path('pdm.lock').exists(): print('yes')")
PDM_INSTALLED=$(shell if pdm --version > /dev/null; then echo "yes"; fi)
VENV_EXISTS=$(shell python3 -c "if __import__('pathlib').Path('.venv/bin/activate').exists(): print('yes')") 
VERSION := $(shell grep -m 1 version pyproject.toml | tr -s ' ' | tr -d '"' | tr -d "'" | cut -d' ' -f3)
BUILD_DIR=dist


.EXPORT_ALL_VARIABLES:

ifndef VERBOSE
.SILENT:
endif


help:													## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)


.PHONY: upgrade
upgrade:												## Upgrade all dependencies to the latest stable versions
	@if [ "$(USING_PDM)" ]; then pdm update; fi
	@echo "Python Dependencies Updated" 
	$(ENV_PREFIX)pre-commit autoupdate
	@echo "Updated Pre-commit"


.PHONY: install
install:												## Install the project in dev mode.
	@if ! pdm --version > /dev/null; then echo 'pdm is required, installing from from https://pdm.fming.dev/'; curl -sSL https://pdm.fming.dev/install-pdm.py | python3 - ; fi
	@if [ "$(VENV_EXISTS)" ]; then echo "Removing existing environment" && rm -Rf .venv;  fi
	@if [ "$(USING_PDM)" ]; then pdm install; fi
	@echo "=> Install complete.  ** If you want to re-install re-run 'make install'"


.PHONY: clean
clean:													## remove all build, testing, and static documentation files
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.ipynb_checkpoints' -exec rm -fr {} +
	find . -name '.terraform' -exec rm -fr {} +
	rm -fr .tox/
	rm -fr .coverage
	rm -fr coverage.xml
	rm -fr coverage.json
	rm -fr htmlcov/
	rm -fr .pytest_cache
	rm -fr .mypy_cache
	rm -fr site

.PHONY: test
test:													## Test project files
	@echo "=> Launching Python test cases..."
	@$(ENV_PREFIX)pytest tests/

.PHONY: lint
lint:													## Lint source files
	@echo "=> Executing pre-commit..."
	@$(ENV_PREFIX)pre-commit run --all-files

.PHONY: build
build:                        							## Install the project in dev mode.
	@echo "=> Building Application..."
	@pdm build
 