from dataclasses import dataclass


@dataclass(frozen=True)


class LendingPolicy:
    """
    Defines the business rules used when evaluating
    loan affordability.
    """

    version: str

    minimum_age: int

    minimum_credit_score: int

    maximum_debt_to_income_ratio: float

    maximum_repayment_to_income_ratio: float

    minimum_disposable_income: float

    maximum_loan_term_months: int

    def is_age_eligible(self, age: int) -> bool:
        return age >= self.minimum_age

    def is_credit_score_eligible(self, score: int) -> bool:
        return score >= self.minimum_credit_score

    def is_debt_to_income_ratio_acceptable(self, ratio: float) -> bool:
        return ratio <= self.maximum_debt_to_income_ratio

    def is_repayment_ratio_acceptable(self, ratio: float) -> bool:
        return ratio <= self.maximum_repayment_to_income_ratio

    def is_disposable_income_acceptable(self, income: float) -> bool:
        return income >= self.minimum_disposable_income