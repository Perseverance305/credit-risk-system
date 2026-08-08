from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class RepaymentResult:
    """Represents the calculated repayment schedule details."""

    monthly_repayment: Decimal
    total_interest: Decimal
    total_repayment: Decimal
    effective_interest_rate: Decimal
    instalments: int
    amortisation_method: str