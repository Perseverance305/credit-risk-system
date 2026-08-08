from abc import ABC, abstractmethod

from app.models.affordability_metrics import AffordabilityMetrics
from app.models.rule_result import RuleResult


class AffordabilityRule(ABC):

    @abstractmethod
    def evaluate(
        self,
        metrics: AffordabilityMetrics
    ) -> RuleResult:
        pass