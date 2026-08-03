from decimal import Decimal
from datetime import date

from app.models.customer import Customer


customer = Customer(
    customer_id="CUST000001",
    first_name="Mogau",
    last_name="Maphanga",
    date_of_birth=date(2001, 8, 15),
    id_number="0108155809084",
    email="mogau@example.com",
    mobile_number="0821234567",
    province="Gauteng",
    employment_status="Full-Time",
    employer="Botsync",
    monthly_income=Decimal("45000"),
    monthly_expenses=Decimal("18000"),
    existing_debt=Decimal("7000"),
    credit_score=720
)

print(customer)

print("\nDisposable Income:")
print(customer.calculate_disposable_income())