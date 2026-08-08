from datetime import date
from decimal import Decimal

from app.composition_root import create_credit_risk_engine
from app.models.customer import Customer
from app.models.loan_application import LoanApplication
from app.services.credit_risk_service import CreditRiskService


def main() -> None:
    engine = create_credit_risk_engine()

    service = CreditRiskService(
        credit_risk_engine=engine,
    )

    customer = Customer(
        customer_id="CUST001",
        first_name="Test",
        last_name="Customer",
        date_of_birth=date(2000, 1, 1),
        id_number="0000000000000",
        email="test@example.com",
        mobile_number="0000000000",
        province="Gauteng",
        employment_status="EMPLOYED",
        employer="Botsync",
        monthly_income=Decimal("30000"),
        monthly_expenses=Decimal("15000"),
        existing_debt=Decimal("5000"),
        credit_score=720,
    )

    loan_application = LoanApplication(
        application_id="APP001",
        customer=customer,
        requested_amount=Decimal("100000"),
        annual_interest_rate=Decimal("12.00"),
        loan_term_months=24,
    )

    result = service.assess(
        customer=customer,
        loan_application=loan_application,
    )

    assert result.passed is True

    assert result.metrics.credit_score == 720
    assert result.metrics.employment_status == "EMPLOYED"
    assert result.metrics.monthly_income == Decimal("30000")
    assert result.metrics.existing_debt == Decimal("5000")
    assert result.metrics.requested_amount == Decimal("100000")
    assert result.metrics.loan_term_months == 24

    assert result.metrics.age == 26

    assert len(result.rule_results) == 3

    for rule_result in result.rule_results:
        assert rule_result.passed is True

    print("Credit risk service tests passed!")


if __name__ == "__main__":
    main()

