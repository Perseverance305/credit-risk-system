from app.config.lending_policy import LendingPolicy
from app.models.credit_risk_metrics import CreditRiskMetrics
from app.models.credit_risk_reason_code import CreditRiskReasonCode
from app.models.rule_result import RuleResult
from app.rules.credit_risk_rule import CreditRiskRule


class LoanTermRule(CreditRiskRule):
    """
    Evaluates whether the requested loan term
    satisfies the lending policy maximum.
    """

    def __init__(self, policy: LendingPolicy) -> None:
        self._policy = policy

    def evaluate(
        self,
        metrics: CreditRiskMetrics,
    ) -> RuleResult:

        loan_term = metrics.loan_term_months

        passed = (
            loan_term
            <= self._policy.maximum_loan_term_months
        )

        reason_code = (
            CreditRiskReasonCode.PASSED
            if passed
            else CreditRiskReasonCode.LOAN_TERM_ABOVE_MAXIMUM
        )

        return RuleResult(
            rule_name="LOAN_TERM",
            passed=passed,
            reason_code=reason_code,
            actual_value=loan_term,
            expected_value=(
                self._policy.maximum_loan_term_months
            ),
            policy_name="LENDING_POLICY",
            policy_version=self._policy.version,
        )

