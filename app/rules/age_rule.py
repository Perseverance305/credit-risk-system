from app.config.lending_policy import LendingPolicy
from app.models.credit_risk_metrics import CreditRiskMetrics
from app.models.credit_risk_reason_code import CreditRiskReasonCode
from app.models.rule_result import RuleResult
from app.rules.credit_risk_rule import CreditRiskRule


class AgeRule(CreditRiskRule):
    """
    Evaluates whether the customer's age
    satisfies the lending policy minimum.
    """

    def __init__(self, policy: LendingPolicy) -> None:
        self._policy = policy

    def evaluate(
        self,
        metrics: CreditRiskMetrics,
    ) -> RuleResult:

        age = metrics.age

        passed = self._policy.is_age_eligible(
            age
        )

        reason_code = (
            CreditRiskReasonCode.PASSED
            if passed
            else CreditRiskReasonCode.AGE_BELOW_MINIMUM
        )

        return RuleResult(
            rule_name="AGE",
            passed=passed,
            reason_code=reason_code,
            actual_value=age,
            expected_value=self._policy.minimum_age,
            policy_name="LENDING_POLICY",
            policy_version=self._policy.version,
        )

