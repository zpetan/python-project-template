# {{ cookiecutter.project_name }}

[![CI Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug}}/actions/workflows/CI.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug}}/actions?query=workflow%3ACI)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

---

**Source Code**: [https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

---

{{ cookiecutter.project_short_description }}

---

## Development

* Clone this repository
* Requirements:
  * Python 3.10+
* Create a virtual environment and install the dependencies

Example using `uv`
```sh
uv sync --all-groups
``````

* Add new packages to `pyproject.toml`

```sh
uv add pandas
```

### Testing

```sh
uv run make pre
uv run pytest
uv run tox
```

### Pre-commit

Pre-commit runs all the auto-formatters (e.g. `black`), linters (e.g. `mypy`, `ruff`), and other quality checks to make sure the changeset is in good shape before a commit/push happens.

To run all checks manually for all files:

```sh
uv run pre-commit run --all-files
```

### Releasing

Before a pull request, trigger the [Draft release workflow](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions/workflows/draft_release.yml)
(press _Run workflow_). Select the feature branch and a version number.

This will update the changelog & version and create a GitHub release which is in _Draft_ state.

Create a pull request with the changes and merge to the main.


Find the draft release from the
[GitHub releases](https://github.com/{{ cookiecutter.github_username}}/{{ cookiecutter.project_slug }}/releases) and publish it.

---
