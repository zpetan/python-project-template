[![CI Status](https://github.com/zpetan/python-project-template/actions/workflows/test.yml/badge.svg)](https://github.com/zpetan/python-project-template/actions)


# Python Package Cookiecutter

A [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/README.html) (project template) for rapidly developing new open source Python packages.


## Features

#### Automatic updates to the projects generated from this cookiecutter

* Powered by [cruft](https://cruft.github.io/cruft/)
* Keep your project up-to-date with best practices

#### Continuous integration

* Powered by [Github Actions](https://github.com/features/actions)
* Testing against multiple different versions

#### Automated releases

* Using Github action workflow

#### Changelog management

* Gently enforced: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
* GitHub releases get their description automatically populated based on the changelog content
* The _Unreleased_ section is automatically updated when a release is done
* Changelog is embedded in the documentation

#### Bells and whistles

* [uv](https://docs.astral.sh/uv/) in Github Actions
* [pre-commit](https://pre-commit.com/) for running all the goodies listed below
* [mypy](https://flake8.pycqa.org/en/latest/) for static type checking
* [ruff](https://github.com/astral-sh/ruff) for linting (e.g. style and complexity checks, commented code, etc.)
* [black](https://black.readthedocs.io/en/stable/) for auto-formatting the code
* [autoflake](https://github.com/myint/autoflake) for auto-removing unused imports

## Usage

Make sure you have [`cruft`](https://github.com/cruft/cruft#installation) installed. Alternatively, you can use
 [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/installation.html) if you are not interested in
  getting updates to the project "boilerplate" in the future.

Create a new project:

```sh
cruft create https://github.com/zpetan/python-data-science-project-cookiecutter_v2
```

The CLI interface will ask some basic questions, such the name of the project, and then generate all the goodies
 automatically.

After that you can make it a proper git repo:

```sh
cd <your-project-slug>
git init
git add .
git commit -m "Initial project structure from python-project-template"
```

Update lates template changes into your project with:

```sh
cruft update
```
