from dataclasses import dataclass
from decimal import Decimal


@dataclass
class AffordabilityResult:
    """
    Represents the outcome of an affordability assessment.
    """

    approved: bool

    disposable_income: Decimal

    debt_to_income_ratio: Decimal

    payment_to_income_ratio: Decimal

    remaining_income: Decimal

    affordability_score: int

    reasons: list[str]