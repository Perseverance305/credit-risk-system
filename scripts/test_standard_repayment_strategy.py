"""Tests for the standard repayment strategy."""

from datetime import date
from decimal import Decimal

from app.models.customer import Customer
from app.models.loan_application import LoanApplication
from app.strategies.repayment.standard_repayment_strategy import (
    StandardRepaymentStrategy,
)


def create_customer() -> Customer:
    return Customer(
        customer_id="C001",
        first_name="Test",
        last_name="Customer",
        date_of_birth=date(1995, 1, 1),
        id_number="9501010000000",
        email="test@example.com",
        mobile_number="0000000000",
        province="Gauteng",
        employment_status="EMPLOYED",
        employer="Test Employer",
        monthly_income=Decimal("20000.00"),
        monthly_expenses=Decimal("8000.00"),
        existing_debt=Decimal("2000.00"),
        credit_score=700,
    )


def test_standard_repayment_with_interest() -> None:
    application = LoanApplication(
        application_id="APP001",
        customer=create_customer(),
        requested_amount=Decimal("10000.00"),
        annual_interest_rate=Decimal("12.00"),
        loan_term_months=12,
    )

    strategy = StandardRepaymentStrategy()

    result = strategy.calculate(application)

    assert result.monthly_repayment == Decimal("888.49")
    assert result.total_repayment == Decimal("10661.88")
    assert result.total_interest == Decimal("661.88")
    assert result.effective_interest_rate == Decimal("12.00")
    assert result.instalments == 12
    assert result.amortisation_method == "AMORTISED"


def test_standard_repayment_with_zero_interest() -> None:
    application = LoanApplication(
        application_id="APP002",
        customer=create_customer(),
        requested_amount=Decimal("12000.00"),
        annual_interest_rate=Decimal("0.00"),
        loan_term_months=12,
    )

    strategy = StandardRepaymentStrategy()

    result = strategy.calculate(application)

    assert result.monthly_repayment == Decimal("1000.00")
    assert result.total_repayment == Decimal("12000.00")
    assert result.total_interest == Decimal("0.00")
    assert result.effective_interest_rate == Decimal("0.00")


def main() -> None:
    test_standard_repayment_with_interest()
    test_standard_repayment_with_zero_interest()

    print("Standard repayment strategy tests passed!")


if __name__ == "__main__":
    main()