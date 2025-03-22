"""Tests Package Version Consistency."""

from {{cookiecutter.package_name}}.core.configs import CONFIG


def test_initial_config() -> None:
    """Checks if config parameter is as expected."""
    assert CONFIG.PARAMETER_01 == "PARAMETER_01"
