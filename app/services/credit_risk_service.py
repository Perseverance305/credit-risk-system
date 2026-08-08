from datetime import date

from app.engines.credit_risk_engine import CreditRiskEngine
from app.models.credit_risk_metrics import CreditRiskMetrics
from app.models.credit_risk_result import CreditRiskResult
from app.models.customer import Customer
from app.models.loan_application import LoanApplication


class CreditRiskService:
    """
    Performs credit risk assessments for loan applications.
    """

    def __init__(
        self,
        credit_risk_engine: CreditRiskEngine,
    ) -> None:
        self.credit_risk_engine = credit_risk_engine

    def assess(
        self,
        customer: Customer,
        loan_application: LoanApplication,
    ) -> CreditRiskResult:
        """
        Assess the credit risk of a loan application.
        """

        age = self._calculate_age(
            customer.date_of_birth
        )

        metrics = CreditRiskMetrics(
            age=age,
            credit_score=customer.credit_score,
            employment_status=customer.employment_status,
            monthly_income=customer.monthly_income,
            existing_debt=customer.existing_debt,
            requested_amount=loan_application.requested_amount,
            loan_term_months=loan_application.loan_term_months,
        )

        return self.credit_risk_engine.evaluate(
            metrics
        )

    @staticmethod
    def _calculate_age(
        date_of_birth: date,
    ) -> int:
        """
        Calculate the customer's current age.
        """

        today = date.today()

        age = (
            today.year
            - date_of_birth.year
            - (
                (today.month, today.day)
                < (date_of_birth.month, date_of_birth.day)
            )
        )

        return age

