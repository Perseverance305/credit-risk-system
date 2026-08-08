from app.config.lending_policy import LendingPolicy
from app.models.affordability_metrics import AffordabilityMetrics
from app.models.affordability_result import AffordabilityResult
from app.rules.affordability_rule import AffordabilityRule


class AffordabilityEngine:

    def __init__(
        self,
        rules: tuple[AffordabilityRule, ...],
        policy: LendingPolicy
    ):
        self._rules = rules
        self._policy = policy

    def evaluate(
        self,
        metrics: AffordabilityMetrics
    ) -> AffordabilityResult:

        rule_results = tuple(
            rule.evaluate(metrics)
            for rule in self._rules
        )

        passed = all(
            result.passed
            for result in rule_results
        )

        return AffordabilityResult(
            passed=passed,
            metrics=metrics,
            rule_results=rule_results,
            policy_version=self._policy.version
        )