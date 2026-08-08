from app.config.lending_policy import LendingPolicy
from app.models.credit_risk_metrics import CreditRiskMetrics
from app.models.credit_risk_reason_code import CreditRiskReasonCode
from app.models.rule_result import RuleResult
from app.rules.credit_risk_rule import CreditRiskRule


class CreditScoreRule(CreditRiskRule):
    """
    Evaluates whether the customer's credit score
    satisfies the lending policy minimum.
    """

    def __init__(self, policy: LendingPolicy) -> None:
        self._policy = policy

    def evaluate(
        self,
        metrics: CreditRiskMetrics,
    ) -> RuleResult:

        score = metrics.credit_score

        passed = self._policy.is_credit_score_eligible(
            score
        )

        reason_code = (
            CreditRiskReasonCode.PASSED
            if passed
            else CreditRiskReasonCode.CREDIT_SCORE_BELOW_MINIMUM
        )

        return RuleResult(
            rule_name="CREDIT_SCORE",
            passed=passed,
            reason_code=reason_code,
            actual_value=score,
            expected_value=self._policy.minimum_credit_score,
            policy_name="LENDING_POLICY",
            policy_version=self._policy.version,
        )

