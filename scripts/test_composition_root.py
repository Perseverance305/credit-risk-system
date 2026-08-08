"""Smoke test for the affordability composition root."""

from app.composition_root import create_affordability_engine
from app.models.affordability_metrics import AffordabilityMetrics


def main() -> None:
    engine = create_affordability_engine()

    metrics = AffordabilityMetrics(
        monthly_income=4000.0,
        monthly_expenses=2000.0,
        existing_debt=800.0,
        disposable_income=1200.0,
        estimated_monthly_repayment=500.0,
        debt_to_income_ratio=0.2,
        repayment_to_income_ratio=0.2,
    )

    result = engine.evaluate(metrics)

    assert result.passed is True
    assert len(result.rule_results) == 3
    assert result.policy_version == "1.0"

    print("Composition root test passed!")


if __name__ == "__main__":
    main()