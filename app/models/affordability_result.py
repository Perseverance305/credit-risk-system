from dataclasses import dataclass

from app.models.affordability_metrics import AffordabilityMetrics
from app.models.rule_result import RuleResult


@dataclass(frozen=True)
class AffordabilityResult:
    """
    Represents the complete result of an affordability assessment.
    """

    passed: bool
    metrics: AffordabilityMetrics
    rule_results: tuple[RuleResult, ...]
    policy_version: str