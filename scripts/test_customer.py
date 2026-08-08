from datetime import date
from decimal import Decimal

from app.models.customer import Customer


def main():
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
        monthly_income=Decimal("45000"),
        monthly_expenses=Decimal("18000"),
        existing_debt=Decimal("7000"),
        credit_score=720,
    )

    print(customer)

    print("\nDisposable Income:")
    print(customer.calculate_disposable_income())


if __name__ == "__main__":
    main()