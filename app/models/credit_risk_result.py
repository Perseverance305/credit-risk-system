from dataclasses import dataclass

from app.models.credit_risk_metrics import CreditRiskMetrics
from app.models.rule_result import RuleResult


@dataclass(frozen=True)
class CreditRiskResult:
    """
    Represents the complete result of a credit risk assessment.
    """

    passed: bool
    metrics: CreditRiskMetrics
    rule_results: tuple[RuleResult, ...]
    policy_version: str

