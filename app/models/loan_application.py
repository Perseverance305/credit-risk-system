from dataclasses import dataclass
from decimal import Decimal

from app.models.customer import Customer


@dataclass
class LoanApplication:
    """Represents a customer's request for a specific loan."""

    application_id: str
    customer: Customer
    requested_amount: Decimal
    annual_interest_rate: Decimal
    loan_term_months: int