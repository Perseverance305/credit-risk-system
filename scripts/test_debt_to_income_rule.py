from app.config.lending_policy import LendingPolicy
from app.models.affordability_metrics import AffordabilityMetrics
from app.models.affordability_reason_code import AffordabilityReasonCode
from app.rules.debt_to_income_rule import DebtToIncomeRule


def test_debt_to_income_passes():

    policy = LendingPolicy(
        minimum_age=18,
        minimum_credit_score=600,
        maximum_debt_to_income_ratio=0.40,
        maximum_repayment_to_income_ratio=0.30,
        minimum_disposable_income=3000.0,
        maximum_loan_term_months=72,
        version="2026.03"
    )

    metrics = AffordabilityMetrics(
        monthly_income=15000.0,
        monthly_expenses=7000.0,
        existing_debt=5250.0,
        disposable_income=8000.0,
        estimated_monthly_repayment=2500.0,
        debt_to_income_ratio=0.35,
        repayment_to_income_ratio=0.17
    )

    rule = DebtToIncomeRule(policy)

    result = rule.evaluate(metrics)

    assert result.passed is True
    assert result.reason_code == AffordabilityReasonCode.PASSED
    assert result.actual_value == 0.35
    assert result.expected_value == 0.40


def test_debt_to_income_fails():

    policy = LendingPolicy(
        minimum_age=18,
        minimum_credit_score=600,
        maximum_debt_to_income_ratio=0.40,
        maximum_repayment_to_income_ratio=0.30,
        minimum_disposable_income=3000.0,
        maximum_loan_term_months=72,
        version="2026.03"
    )

    metrics = AffordabilityMetrics(
        monthly_income=15000.0,
        monthly_expenses=7000.0,
        existing_debt=6750.0,
        disposable_income=8000.0,
        estimated_monthly_repayment=2500.0,
        debt_to_income_ratio=0.45,
        repayment_to_income_ratio=0.17
    )

    rule = DebtToIncomeRule(policy)

    result = rule.evaluate(metrics)

    assert result.passed is False
    assert result.reason_code == (
        AffordabilityReasonCode.DTI_ABOVE_MAXIMUM
    )
    assert result.actual_value == 0.45
    assert result.expected_value == 0.40


if __name__ == "__main__":
    test_debt_to_income_passes()
    test_debt_to_income_fails()
    print("Debt-to-income rule tests passed!")