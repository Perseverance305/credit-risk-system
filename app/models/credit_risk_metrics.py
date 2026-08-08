from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class CreditRiskMetrics:
    """
    Represents the risk-relevant metrics used
    during a credit risk assessment.
    """

    age: int
    credit_score: int
    employment_status: str
    monthly_income: Decimal
    existing_debt: Decimal
    requested_amount: Decimal
    loan_term_months: int

