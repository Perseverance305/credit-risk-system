from decimal import Decimal

from app.contracts.repayment_strategy import RepaymentStrategy
from app.models.loan_application import LoanApplication
from app.models.repayment_result import RepaymentResult


class StandardRepaymentStrategy(RepaymentStrategy):
    """Standard amortising loan repayment strategy."""

    def calculate(
        self,
        application: LoanApplication
    ) -> RepaymentResult:

        monthly_repayment = self._calculate_monthly_repayment(
            application
        )

        total_repayment = self._calculate_total_repayment(
            application,
            monthly_repayment
        )

        total_interest = self._calculate_total_interest(
            total_repayment,
            application
        )

        return RepaymentResult(
            monthly_repayment=monthly_repayment,
            total_interest=total_interest,
            total_repayment=total_repayment,
            effective_interest_rate=application.annual_interest_rate,
            instalments=application.loan_term_months,
            amortisation_method="AMORTISED"
        )

    def _calculate_monthly_repayment(
        self,
        application: LoanApplication
    ) -> Decimal:

        principal = application.requested_amount
        annual_rate = application.annual_interest_rate
        term_months = application.loan_term_months

        monthly_rate = (
            annual_rate
            / Decimal("12")
            / Decimal("100")
        )

        if monthly_rate == Decimal("0"):
            return (
                principal
                / Decimal(term_months)
            ).quantize(Decimal("0.01"))

        growth_factor = (
            Decimal("1") + monthly_rate
        ) ** term_months

        monthly_repayment = (
            principal
            * monthly_rate
            * growth_factor
            / (growth_factor - Decimal("1"))
        )

        return monthly_repayment.quantize(
            Decimal("0.01")
        )

    def _calculate_total_repayment(
        self,
        application: LoanApplication,
        monthly_repayment: Decimal
    ) -> Decimal:

        total_repayment = (
            monthly_repayment
            * Decimal(application.loan_term_months)
        )

        return total_repayment.quantize(
            Decimal("0.01")
        )

    def _calculate_total_interest(
        self,
        total_repayment: Decimal,
        application: LoanApplication
    ) -> Decimal:

        total_interest = (
            total_repayment
            - application.requested_amount
        )

        return total_interest.quantize(
            Decimal("0.01")
        )