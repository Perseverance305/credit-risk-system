"""Smoke test for the affordability engine."""

from app.config.lending_policy import LendingPolicy
from app.engines.affordability_engine import AffordabilityEngine
from app.models.affordability_metrics import AffordabilityMetrics
from app.models.affordability_reason_code import AffordabilityReasonCode
from app.rules.disposable_income_rule import DisposableIncomeRule
from app.rules.debt_to_income_rule import DebtToIncomeRule
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

    rules = (
        DisposableIncomeRule(policy),
        DebtToIncomeRule(policy),
        RepaymentBurdenRule(policy),
    )

    engine = AffordabilityEngine(
        rules=rules,
        policy=policy,
    )

    # ---------------------------------------------------------
    # Scenario 1: All affordability rules pass
    # ---------------------------------------------------------

    passing_metrics = AffordabilityMetrics(
        monthly_income=4000.0,
        monthly_expenses=2000.0,
        existing_debt=800.0,
        disposable_income=1200.0,
        estimated_monthly_repayment=500.0,
        debt_to_income_ratio=0.2,
        repayment_to_income_ratio=0.2,
    )

    passing_result = engine.evaluate(passing_metrics)

    assert passing_result.passed is True
    assert len(passing_result.rule_results) == 3
    assert all(
        rule_result.passed
        for rule_result in passing_result.rule_results
    )
    assert passing_result.policy_version == "1.0"

    # ---------------------------------------------------------
    # Scenario 2: Repayment burden fails
    # ---------------------------------------------------------

    failing_metrics = AffordabilityMetrics(
        monthly_income=4000.0,
        monthly_expenses=2000.0,
        existing_debt=800.0,
        disposable_income=1200.0,
        estimated_monthly_repayment=1400.0,
        debt_to_income_ratio=0.2,
        repayment_to_income_ratio=0.35,
    )

    failing_result = engine.evaluate(failing_metrics)

    assert failing_result.passed is False
    assert len(failing_result.rule_results) == 3
    assert failing_result.policy_version == "1.0"

    # Verify that the repayment burden specialist
    # produced the failure.
    repayment_burden_result = next(
        result
        for result in failing_result.rule_results
        if result.rule_name == "RepaymentBurdenRule"
    )

    assert repayment_burden_result.passed is False
    assert (
        repayment_burden_result.reason_code
        == AffordabilityReasonCode.REPAYMENT_BURDEN_ABOVE_MAXIMUM
    )
    assert repayment_burden_result.actual_value == 0.35
    assert repayment_burden_result.expected_value == 0.3

    print("Affordability engine tests passed!")


if __name__ == "__main__":
    main()