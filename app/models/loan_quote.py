class LoanQuote:

    def __init__(
        self,
        monthly_payment,
        total_interest,
        total_repayment,
        interest_rate,
        term_months,
    ):
        self.monthly_payment = monthly_payment
        self.total_interest = total_interest
        self.total_repayment = total_repayment
        self.interest_rate = interest_rate
        self.term_months = term_months