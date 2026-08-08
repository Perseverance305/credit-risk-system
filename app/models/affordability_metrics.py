from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class AffordabilityMetrics:
    """
    Represents the financial metrics calculated during
    an affordability assessment.
    """

    monthly_income: Decimal
    monthly_expenses: Decimal
    existing_debt: Decimal
    disposable_income: Decimal
    estimated_monthly_repayment: Decimal
    debt_to_income_ratio: Decimal
    repayment_to_income_ratio: Decimal