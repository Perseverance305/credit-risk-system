from decimal import Decimal

from app.config.lending_policy import LendingPolicy
from app.models.affordability_metrics import AffordabilityMetrics
from app.models.affordability_reason_code import AffordabilityReasonCode
from app.models.affordability_result import AffordabilityResult
from app.models.customer import Customer
from app.models.loan_application import LoanApplication
from app.models.rule_result import RuleResult
from app.utils.repayment_calculator import RepaymentCalculator
from app.engines.affordability_engine import AffordabilityEngine


class AffordabilityService:
    """
    Performs affordability assessments for loan applications.
    """

    def __init__(
        self,
        repayment_calculator: RepaymentCalculator,
        affordability_engine: AffordabilityEngine,
    ):
        self.repayment_calculator = repayment_calculator
        self.affordability_engine = affordability_engine

    def assess(
        self,
        customer: Customer,
        loan_application: LoanApplication,
    ) -> AffordabilityResult:
        """
        Assess whether the customer can afford the requested loan.
        """

        disposable_income = customer.calculate_disposable_income()

        repayment_result = self.repayment_calculator.calculate(
            loan_application
        )

        if customer.monthly_income == Decimal("0"):
            debt_to_income_ratio = Decimal("Infinity")
            repayment_to_income_ratio = Decimal("Infinity")
        else:
            debt_to_income_ratio = (
                customer.existing_debt
                / customer.monthly_income
            )

            repayment_to_income_ratio = (
                repayment_result.monthly_repayment
                / customer.monthly_income
            )

        metrics = AffordabilityMetrics(
            monthly_income=customer.monthly_income,
            monthly_expenses=customer.monthly_expenses,
            existing_debt=customer.existing_debt,
            disposable_income=disposable_income,
            estimated_monthly_repayment=(
                repayment_result.monthly_repayment
            ),
            debt_to_income_ratio=debt_to_income_ratio,
            repayment_to_income_ratio=(
                repayment_to_income_ratio
            ),

        )

        return self.affordability_engine.evaluate(metrics)

    