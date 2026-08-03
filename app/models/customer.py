class Customer:
    def __init__(self, customer_id, name, credit_score, annual_income):
        self.customer_id = customer_id
        self.name = name
        self.credit_score = credit_score
        self.annual_income = annual_income

    def __repr__(self):
        return (
            f"Customer(customer_id={self.customer_id!r}, name={self.name!r}, "
            f"credit_score={self.credit_score!r}, annual_income={self.annual_income!r})"
        )
