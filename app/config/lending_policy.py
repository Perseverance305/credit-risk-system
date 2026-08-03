from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class LendingPolicy:
    """
    Lending policy thresholds.
    """

    minimum_disposable_income: Decimal = Decimal("2500")

    maximum_debt_to_income_ratio: Decimal = Decimal("0.40")

    maximum_payment_to_income_ratio: Decimal = Decimal("0.30")

    minimum_credit_score: int = 620