from abc import ABC, abstractmethod

from app.models.credit_risk_metrics import CreditRiskMetrics
from app.models.rule_result import RuleResult


class CreditRiskRule(ABC):
    """
    Defines the contract for credit risk rules.
    """

    @abstractmethod
    def evaluate(
        self,
        metrics: CreditRiskMetrics,
    ) -> RuleResult:
        """
        Evaluate the credit risk rule against the supplied metrics.
        """
        raise NotImplementedError

