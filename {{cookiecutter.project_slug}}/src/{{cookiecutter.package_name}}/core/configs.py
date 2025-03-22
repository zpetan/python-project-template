"""Project configurations."""

from dataclasses import dataclass

__all__ = ["CONFIG"]


@dataclass(frozen=True)
class _Configs:
    """Configuration definitions."""

    PARAMETER_01: str = "PARAMETER_01"


# Import this
CONFIG = _Configs()
