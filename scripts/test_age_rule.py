"""Smoke tests for the age rule."""

from app.config.lending_policy import LendingPolicy
from app.models.credit_risk_metrics import CreditRiskMetrics
from app.models.credit_risk_reason_code import CreditRiskReasonCode
from app.rules.age_rule import AgeRule


def main() -> None:
    policy = LendingPolicy(
        version="1.0",
        minimum_age=18,
        minimum_credit_score=600,
        maximum_debt_to_income_ratio=0.4,
        maximum_repayment_to_income_ratio=0.3,
        minimum_disposable_income=1000.0,
        maximum_loan_term_months=60,
    )

    passing_metrics = CreditRiskMetrics(
        age=30,
        credit_score=720,
        employment_status="EMPLOYED",
        monthly_income=30000,
        existing_debt=5000,
        requested_amount=100000,
        loan_term_months=24,
    )

    failing_metrics = CreditRiskMetrics(
        age=17,
        credit_score=720,
        employment_status="EMPLOYED",
        monthly_income=30000,
        existing_debt=5000,
        requested_amount=100000,
        loan_term_months=24,
    )

    rule = AgeRule(policy)

    passing_result = rule.evaluate(passing_metrics)
    failing_result = rule.evaluate(failing_metrics)

    assert passing_result.passed is True
    assert passing_result.reason_code == (
        CreditRiskReasonCode.PASSED
    )
    assert passing_result.actual_value == 30

    assert failing_result.passed is False
    assert failing_result.reason_code == (
        CreditRiskReasonCode.AGE_BELOW_MINIMUM
    )
    assert failing_result.actual_value == 17

    print("Age rule tests passed!")


if __name__ == "__main__":
    main()
