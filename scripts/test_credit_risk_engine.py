"""Smoke tests for the credit risk engine."""

from app.config.lending_policy import LendingPolicy
from app.engines.credit_risk_engine import CreditRiskEngine
from app.models.credit_risk_metrics import CreditRiskMetrics
from app.models.credit_risk_reason_code import CreditRiskReasonCode
from app.rules.age_rule import AgeRule
from app.rules.credit_score_rule import CreditScoreRule
from app.rules.loan_term_rule import LoanTermRule


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

    rules = (
        CreditScoreRule(policy),
        AgeRule(policy),
        LoanTermRule(policy),
    )

    engine = CreditRiskEngine(
        rules=rules,
        policy=policy,
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

    result = engine.evaluate(passing_metrics)

    assert result.passed is True
    assert result.policy_version == "1.0"
    assert len(result.rule_results) == 3

    for rule_result in result.rule_results:
        assert rule_result.passed is True
        assert rule_result.reason_code == (
            CreditRiskReasonCode.PASSED
        )

    failing_metrics = CreditRiskMetrics(
        age=17,
        credit_score=550,
        employment_status="EMPLOYED",
        monthly_income=30000,
        existing_debt=5000,
        requested_amount=100000,
        loan_term_months=72,
    )

    result = engine.evaluate(failing_metrics)

    assert result.passed is False
    assert len(result.rule_results) == 3

    assert result.rule_results[0].passed is False
    assert result.rule_results[0].reason_code == (
        CreditRiskReasonCode.CREDIT_SCORE_BELOW_MINIMUM
    )

    assert result.rule_results[1].passed is False
    assert result.rule_results[1].reason_code == (
        CreditRiskReasonCode.AGE_BELOW_MINIMUM
    )

    assert result.rule_results[2].passed is False
    assert result.rule_results[2].reason_code == (
        CreditRiskReasonCode.LOAN_TERM_ABOVE_MAXIMUM
    )

    print("Credit risk engine tests passed!")


if __name__ == "__main__":
    main()

