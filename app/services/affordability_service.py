from decimal import Decimal

from app.models.customer import Customer
from app.models.loan_application import LoanApplication
from app.models.affordability_result import AffordabilityResult


class AffordabilityService:
    """
    Performs affordability assessments for loan applications.
    """

    def assess(
        self,
        customer: Customer,
        loan_application: LoanApplication,
    ) -> AffordabilityResult:
        """
        Assess whether the customer can afford the requested loan.
        """

        raise NotImplementedError("Assessment logic will be added next.")