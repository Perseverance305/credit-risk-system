from dataclasses import dataclass


@dataclass
class AffordabilityResult:
    """Represents the business decision/result of an affordability assessment."""

    passed: bool
    failure_reasons: list[str]
    warnings: list[str]
    policy_version: str