class IncomeTaxCalculator:

    def __init__(self):
        self.salary = 0
        self.salary_income = 0
        self.other_income = 0
        self.bank_interest = 0
        self.tax_regime = ""
        self.tds_paid = 0

    def get_input(self):

        print("========== Income Tax Calculator ==========")

        self.salary = float(input("1. Annual Salary: ₹"))
        self.tax_regime = input("2. Tax Regime (old/new): ").strip().lower()

        self.salary_income = float(input("3. Income from Salary: ₹"))
        self.other_income = float(input("4. Income from Other Sources: ₹"))
        self.bank_interest = float(input("5. Income from Bank Interest / FD: ₹"))

        self.tds_paid = float(input("6. Tax Already Paid (TDS): ₹"))

    def get_standard_deduction(self):

        # FY 2025-26
        if self.tax_regime == "new":
            return 75000
        else:
            return 50000

    def taxable_income(self):

        gross = (
            self.salary_income
            + self.other_income
            + self.bank_interest
        )

        deduction = self.get_standard_deduction()

        taxable = max(0, gross - deduction)

        return taxable

    def calculate_tax(self, income):

        tax = 0

        if self.tax_regime == "new":

            slabs = [
                (400000, 0),
                (800000, 0.05),
                (1200000, 0.10),
                (1600000, 0.15),
                (2000000, 0.20),
                (2400000, 0.25),
            ]

            previous = 0

            for limit, rate in slabs:

                if income > limit:
                    tax += (limit - previous) * rate
                    previous = limit
                else:
                    tax += (income - previous) * rate
                    return max(0, tax)

            tax += (income - 2400000) * 0.30

        else:

            if income <= 250000:
                tax = 0

            elif income <= 500000:
                tax = (income - 250000) * 0.05

            elif income <= 1000000:
                tax = (
                    250000 * 0.05
                    + (income - 500000) * 0.20
                )

            else:
                tax = (
                    250000 * 0.05
                    + 500000 * 0.20
                    + (income - 1000000) * 0.30
                )

        return tax

    def print_summary(self):

        taxable = self.taxable_income()

        tax = self.calculate_tax(taxable)

        cess = tax * 0.04

        total_tax = tax + cess

        balance = total_tax - self.tds_paid

        print("\n========== TAX SUMMARY ==========")

        print(f"Tax Regime                 : {self.tax_regime.title()}")
        print(f"Gross Income               : ₹{self.salary_income + self.other_income + self.bank_interest:,.2f}")
        print(f"Standard Deduction         : ₹{self.get_standard_deduction():,.2f}")
        print(f"Total Taxable Income       : ₹{taxable:,.2f}")
        print(f"Income Tax                 : ₹{tax:,.2f}")
        print(f"Health & Education Cess    : ₹{cess:,.2f}")
        print(f"Total Tax                  : ₹{total_tax:,.2f}")
        print(f"Tax Already Paid (TDS)     : ₹{self.tds_paid:,.2f}")

        if balance > 0:
            print(f"Balance Tax Payable        : ₹{balance:,.2f}")
            print("Refund                     : ₹0.00")
        else:
            print("Balance Tax Payable        : ₹0.00")
            print(f"Refund                     : ₹{-balance:,.2f}")


if __name__ == "__main__":

    calculator = IncomeTaxCalculator()

    calculator.get_input()

    calculator.print_summary()
