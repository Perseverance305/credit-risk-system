from app.config.lending_policy import LendingPolicy
from app.models.affordability_metrics import AffordabilityMetrics
from app.models.affordability_reason_code import AffordabilityReasonCode
from app.models.rule_result import RuleResult
from app.rules.affordability_rule import AffordabilityRule



class DisposableIncomeRule(AffordabilityRule):

    def __init__(self, policy: LendingPolicy):
        self._policy = policy

    def evaluate(
        self,
        metrics: AffordabilityMetrics
    ) -> RuleResult:

        income = metrics.disposable_income

        passed = self._policy.is_disposable_income_acceptable(
            income
        )

        reason_code = (
            AffordabilityReasonCode.PASSED
            if passed
            else AffordabilityReasonCode.DISPOSABLE_INCOME_BELOW_MINIMUM
        )

        return RuleResult(
            rule_name="DisposableIncomeRule",
            passed=passed,
            reason_code=reason_code,
            actual_value=income,
            expected_value=self._policy.minimum_disposable_income,
            policy_name="STANDARD_LENDING_POLICY",
            policy_version="CURRENT"
        )