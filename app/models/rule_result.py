from dataclasses import dataclass
from typing import Any

from app.models.affordability_reason_code import AffordabilityReasonCode


@dataclass(frozen=True)
class RuleResult:
    rule_name: str
    passed: bool
    reason_code: AffordabilityReasonCode
    actual_value: Any
    expected_value: Any
    policy_name: str
    policy_version: str