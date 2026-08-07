from app.contracts.repayment_strategy import RepaymentStrategy
from app.models.loan_application import LoanApplication
from app.models.repayment_result import RepaymentResult


class RepaymentCalculator:
    """
    Coordinates repayment calculations using the configured strategy.
    """

    def __init__(
        self,
        strategy: RepaymentStrategy
    ) -> None:
        self._strategy = strategy

    def calculate(
        self,
        application: LoanApplication
    ) -> RepaymentResult:
        return self._strategy.calculate(application)