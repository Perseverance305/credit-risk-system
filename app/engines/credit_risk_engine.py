from app.config.lending_policy import LendingPolicy
from app.models.credit_risk_metrics import CreditRiskMetrics
from app.models.credit_risk_result import CreditRiskResult
from app.rules.credit_risk_rule import CreditRiskRule


class CreditRiskEngine:
    """
    Coordinates the evaluation of credit risk rules.
    """

    def __init__(
        self,
        rules: tuple[CreditRiskRule, ...],
        policy: LendingPolicy,
    ) -> None:
        self._rules = rules
        self._policy = policy

    def evaluate(
        self,
        metrics: CreditRiskMetrics,
    ) -> CreditRiskResult:

        rule_results = tuple(
            rule.evaluate(metrics)
            for rule in self._rules
        )

        passed = all(
            result.passed
            for result in rule_results
        )

        return CreditRiskResult(
            passed=passed,
            metrics=metrics,
            rule_results=rule_results,
            policy_version=self._policy.version,
        )

