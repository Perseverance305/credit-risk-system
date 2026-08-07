from app.contracts.repayment_strategy import RepaymentStrategy
from app.models.loan_application import LoanApplication
from app.models.repayment_result import RepaymentResult
import math


class StandardRepaymentStrategy(RepaymentStrategy):
    """
    Standard amortising loan repayment strategy.
    """

    def calculate(
        self,
        application: LoanApplication
    ) -> RepaymentResult:

        monthly_repayment = self._calculate_monthly_repayment(
            application
        )

        total_interest = self._calculate_total_interest(
            application,
            monthly_repayment
        )

        total_repayment = self._calculate_total_repayment(
            monthly_repayment,
            application
            
        )

        return RepaymentResult(
            monthly_repayment=monthly_repayment,
            total_interest=total_interest,
            total_repayment=total_repayment,
            effective_interest_rate=0.0,
            instalments=application.loan_term_months,
            amortisation_method="Standard"
        )
# 1. Establish the monthly repayment

def _calculate_monthly_repayment(
    self,
    application: LoanApplication
) -> float:

    principal = application.requested_amount
    annual_rate = application.annual_interest_rate
    term_months = application.loan_term_months

    monthly_rate = annual_rate / 1200

    if math.isclose(monthly_rate, 0.0):
        return principal / term_months

    growth_factor = (1 + monthly_rate) ** term_months

    numerator = monthly_rate * growth_factor
    denominator = growth_factor - 1

    monthly_payment = principal * (numerator / denominator)

    return monthly_payment

        raise NotImplementedError

# 2. Establish the total interest

def _calculate_total_interest(
    self,
    application: LoanApplication,
    monthly_repayment: float
) -> float:

    total_repayment = (
        monthly_repayment
        * application.loan_term_months
    )

    return total_repayment - application.requested_amount
        raise NotImplementedError

# 3. Establish the total repayment

def _calculate_total_repayment(
    application: LoanApplication,
    total_interest: float
) -> float:
        raise NotImplementedError

# 4. Record the repayment result
    return RepaymentResult(...)   