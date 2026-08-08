"""Base interface for repayment strategies."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.loan_application import LoanApplication
    from app.models.repayment_result import RepaymentResult


class RepaymentStrategy(ABC):
    """Defines the contract for repayment calculation strategies."""

    @abstractmethod
    def calculate(self, application: "LoanApplication") -> "RepaymentResult":
        """Calculate repayment details for the given application."""
        raise NotImplementedError
