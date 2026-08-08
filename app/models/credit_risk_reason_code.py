from enum import Enum


class CreditRiskReasonCode(str, Enum):
    """
    Defines the reason codes produced by credit risk rules.
    """

    PASSED = "PASSED"

    CREDIT_SCORE_BELOW_MINIMUM = (
        "CREDIT_SCORE_BELOW_MINIMUM"
    )

    AGE_BELOW_MINIMUM = (
        "AGE_BELOW_MINIMUM"
    )

    LOAN_TERM_ABOVE_MAXIMUM = (
        "LOAN_TERM_ABOVE_MAXIMUM"
    )

