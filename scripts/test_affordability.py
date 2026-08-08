from datetime import date
from decimal import Decimal

from app.config.lending_policy import LendingPolicy
from app.models.customer import Customer
from app.models.loan_application import LoanApplication
from app.services.affordability_service import AffordabilityService
from app.services.repayment_service import RepaymentService


def main():
    policy = LendingPolicy(
        version="2026.08",
        minimum_age=18,
        minimum_credit_score=600,
        maximum_debt_to_income_ratio=0.40,
        maximum_repayment_to_income_ratio=0.30,
        minimum_disposable_income=5000.00,
        maximum_loan_term_months=72,
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
        monthly_expenses=Decimal("20000"),
        existing_debt=Decimal("10000"),
        credit_score=720,
    )

    loan_application = LoanApplication(
        application_id="APP001",
        customer=customer,
        requested_amount=Decimal("100000.00"),
        annual_interest_rate=Decimal("12.00"),
        loan_term_months=24,
    )

    repayment_service = RepaymentService()

    affordability_service = AffordabilityService(
        policy=policy,
        repayment_service=repayment_service,
    )

    result = affordability_service.assess(
        customer=customer,
        loan_application=loan_application,
    )

    print("Affordability decision:", result.passed)
    print("Policy version:", result.policy_version)

    print("\nAffordability Metrics:")
    print("Monthly income:", result.metrics.monthly_income)
    print("Monthly expenses:", result.metrics.monthly_expenses)
    print("Existing debt:", result.metrics.existing_debt)
    print("Disposable income:", result.metrics.disposable_income)
    print(
        "Estimated monthly repayment:",
        result.metrics.estimated_monthly_repayment,
    )
    print(
        "Debt-to-income ratio:",
        result.metrics.debt_to_income_ratio,
    )
    print(
        "Repayment-to-income ratio:",
        result.metrics.repayment_to_income_ratio,
    )

    print("\nRule Results:")

    for rule in result.rule_results:
        print(f"\nRule: {rule.rule_name}")
        print(f"Passed: {rule.passed}")
        print(f"Reason: {rule.reason_code.value}")
        print(f"Actual value: {rule.actual_value}")
        print(f"Expected value: {rule.expected_value}")


if __name__ == "__main__":
    main()