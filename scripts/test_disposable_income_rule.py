from app.config.lending_policy import LendingPolicy
from app.models.affordability_metrics import AffordabilityMetrics
from app.models.affordability_reason_code import AffordabilityReasonCode
from app.rules.disposable_income_rule import DisposableIncomeRule



def test_disposable_income_passes():
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
        monthly_expenses=8000.0,
        existing_debt=2000.0,
        disposable_income=5000.0,
        estimated_monthly_repayment=2500.0,
        debt_to_income_ratio=0.35,
        repayment_to_income_ratio=0.17
    )

    rule = DisposableIncomeRule(policy)

    result = rule.evaluate(metrics)

    assert result.passed is True
    assert result.reason_code == AffordabilityReasonCode.PASSED
    assert result.actual_value == 5000.0
    assert result.expected_value == 3000.0


def test_disposable_income_fails():
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
        monthly_income=12000.0,
        monthly_expenses=9500.0,
        existing_debt=2000.0,
        disposable_income=2500.0,
        estimated_monthly_repayment=2500.0,
        debt_to_income_ratio=0.35,
        repayment_to_income_ratio=0.21
    )

    rule = DisposableIncomeRule(policy)

    result = rule.evaluate(metrics)

    assert result.passed is False
    assert result.reason_code == (
        AffordabilityReasonCode.DISPOSABLE_INCOME_BELOW_MINIMUM
    )
    assert result.actual_value == 2500.0
    assert result.expected_value == 3000.0


if __name__ == "__main__":
    test_disposable_income_passes()
    test_disposable_income_fails()
    print("Disposable income rule tests passed!")