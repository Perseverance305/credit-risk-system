from app.config.lending_policy import LendingPolicy
from app.models.affordability_metrics import AffordabilityMetrics
from app.models.affordability_reason_code import AffordabilityReasonCode
from app.models.rule_result import RuleResult
from app.rules.affordability_rule import AffordabilityRule


class RepaymentBurdenRule(AffordabilityRule):

    def __init__(self, policy: LendingPolicy):
        self._policy = policy

    def evaluate(
        self,
        metrics: AffordabilityMetrics
    ) -> RuleResult:

        ratio = metrics.repayment_to_income_ratio

        passed = self._policy.is_repayment_ratio_acceptable(
            ratio
        )

        reason_code = (
            AffordabilityReasonCode.PASSED
            if passed
            else AffordabilityReasonCode.REPAYMENT_BURDEN_ABOVE_MAXIMUM
        )

        return RuleResult(
            rule_name="RepaymentBurdenRule",
            passed=passed,
            reason_code=reason_code,
            actual_value=ratio,
            expected_value=self._policy.maximum_repayment_to_income_ratio,
            policy_name="STANDARD_LENDING_POLICY",
            policy_version=self._policy.version
        )