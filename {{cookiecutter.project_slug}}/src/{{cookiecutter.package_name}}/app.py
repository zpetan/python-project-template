"""Main routine."""

from {{cookiecutter.package_name}}.core.configs import CONFIG
from {{cookiecutter.package_name}}.core.log_config import get_logger

__all__ = ["main"]


def main() -> None:
    """Main routine of {{ cookiecutter.project_name }}."""
    logger = get_logger(__name__)
    logger.info("Hello, world!")
    logger.debug("This is {{cookiecutter.package_name}}.")
    logger.debug(f"CONFIG: {CONFIG}")  # noqa: G004


if __name__ == "__main__":
    main()
