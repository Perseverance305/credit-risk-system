"""Smoke test for the repayment burden affordability rule."""

from app.config.lending_policy import LendingPolicy
from app.models.affordability_metrics import AffordabilityMetrics
from app.models.affordability_reason_code import AffordabilityReasonCode
from app.rules.repayment_burden_rule import RepaymentBurdenRule


def main() -> None:
    policy = LendingPolicy(
        version="1.0",
        minimum_age=18,
        minimum_credit_score=300,
        maximum_debt_to_income_ratio=0.4,
        maximum_repayment_to_income_ratio=0.3,
        minimum_disposable_income=1000.0,
        maximum_loan_term_months=60,
    )

    # Scenario 1: Repayment burden is within policy limit
    passing_metrics = AffordabilityMetrics(
        monthly_income=4000.0,
        monthly_expenses=2000.0,
        existing_debt=800.0,
        disposable_income=1200.0,
        estimated_monthly_repayment=500.0,
        debt_to_income_ratio=0.2,
        repayment_to_income_ratio=0.2,
    )

    # Scenario 2: Repayment burden exceeds policy limit
    failing_metrics = AffordabilityMetrics(
        monthly_income=3000.0,
        monthly_expenses=2500.0,
        existing_debt=900.0,
        disposable_income=500.0,
        estimated_monthly_repayment=600.0,
        debt_to_income_ratio=0.3,
        repayment_to_income_ratio=0.35,
    )

    rule = RepaymentBurdenRule(policy)

    passing_result = rule.evaluate(passing_metrics)
    failing_result = rule.evaluate(failing_metrics)

    # Passing scenario
    assert passing_result.passed is True
    assert passing_result.reason_code == AffordabilityReasonCode.PASSED
    assert passing_result.actual_value == 0.2
    assert passing_result.expected_value == 0.3
    assert passing_result.policy_version == "1.0"

    # Failing scenario
    assert failing_result.passed is False
    assert (
        failing_result.reason_code
        == AffordabilityReasonCode.REPAYMENT_BURDEN_ABOVE_MAXIMUM
    )
    assert failing_result.actual_value == 0.35
    assert failing_result.expected_value == 0.3
    assert failing_result.policy_version == "1.0"

    print("Repayment burden rule tests passed!")


if __name__ == "__main__":
    main()