from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class Customer:
    """
    Represents a customer applying for a loan.
    """

    customer_id: str
    first_name: str
    last_name: str
    date_of_birth: date
    id_number: str
    email: str
    mobile_number: str
    province: str

    employment_status: str
    employer: str

    monthly_income: Decimal
    monthly_expenses: Decimal
    existing_debt: Decimal

    credit_score: int

    def calculate_disposable_income(self) -> Decimal:
        """
        Calculates disposable monthly income.
        """

        return (
            self.monthly_income
            - self.monthly_expenses
            - self.existing_debt
        )