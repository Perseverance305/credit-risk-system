from app.config.lending_policy import LendingPolicy
from app.engines.affordability_engine import AffordabilityEngine
from app.rules.debt_to_income_rule import DebtToIncomeRule
from app.rules.disposable_income_rule import DisposableIncomeRule
from app.rules.repayment_burden_rule import RepaymentBurdenRule
from app.services.affordability_service import AffordabilityService
from app.strategies.repayment.standard_repayment_strategy import (
    StandardRepaymentStrategy,
)
from app.utils.repayment_calculator import RepaymentCalculator
from app.engines.credit_risk_engine import CreditRiskEngine
from app.rules.age_rule import AgeRule
from app.rules.credit_score_rule import CreditScoreRule
from app.rules.loan_term_rule import LoanTermRule
from app.services.credit_risk_service import CreditRiskService


def create_lending_policy() -> LendingPolicy:
    return LendingPolicy(
        version="1.0",
        minimum_age=18,
        minimum_credit_score=300,
        maximum_debt_to_income_ratio=0.4,
        maximum_repayment_to_income_ratio=0.3,
        minimum_disposable_income=1000.0,
        maximum_loan_term_months=60,
    )


def create_affordability_engine(
    policy: LendingPolicy | None = None,
) -> AffordabilityEngine:

    if policy is None:
        policy = create_lending_policy()

    rules = (
        DisposableIncomeRule(policy),
        DebtToIncomeRule(policy),
        RepaymentBurdenRule(policy),
    )

    return AffordabilityEngine(
        rules=rules,
        policy=policy,
    )


def create_credit_risk_engine(
    policy: LendingPolicy | None = None,
) -> CreditRiskEngine:

    if policy is None:
        policy = create_lending_policy()

    rules = (
        CreditScoreRule(policy),
        AgeRule(policy),
        LoanTermRule(policy),
    )

    return CreditRiskEngine(
        rules=rules,
        policy=policy,
    )


def create_credit_risk_service() -> CreditRiskService:

    credit_risk_engine = create_credit_risk_engine()

    return CreditRiskService(
        credit_risk_engine=credit_risk_engine,
    )



def create_repayment_calculator() -> RepaymentCalculator:

    strategy = StandardRepaymentStrategy()

    return RepaymentCalculator(
        strategy=strategy,
    )


def create_affordability_service() -> AffordabilityService:

    policy = create_lending_policy()

    affordability_engine = create_affordability_engine(
        policy=policy,
    )

    repayment_calculator = create_repayment_calculator()

    return AffordabilityService(
        repayment_calculator=repayment_calculator,
        affordability_engine=affordability_engine,
    )




