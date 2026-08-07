from dataclasses import dataclass


@dataclass(frozen=True)
class AffordabilityMetrics:
    monthly_income: float
    monthly_expenses: float
    existing_debt: float
    disposable_income: float
    estimated_monthly_repayment: float
    debt_to_income_ratio: float
    repayment_to_income_ratio: float
