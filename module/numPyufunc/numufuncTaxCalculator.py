class IncomeTaxCalculator:

    def __init__(self):
        self.salary = 0
        self.salary_income = 0
        self.other_income = 0
        self.bank_interest = 0
        self.tax_regime = ""
        self.tds_paid = 0

    def get_input(self):

        print("=" * 75)
        print("             INDIAN INCOME TAX CALCULATOR (FY 2025-26)")
        print("=" * 75)

        print("\nPlease keep the following documents ready:")
        print("  ✓ Form 16")
        print("  ✓ Form 26AS")
        print("  ✓ Annual Information Statement (AIS)")
        print("  ✓ Bank Interest / FD Certificates")
        print("  ✓ Salary Slip")
        print()

        print("-" * 75)
        print("[Step 1] Annual Salary")
        print("-" * 75)
        print("Enter your Annual Gross Salary (NOT Monthly Salary).")
        self.salary = float(input("Annual Salary (₹): "))

        print("\n" + "-" * 75)
        print("[Step 2] Select Tax Regime")
        print("-" * 75)
        print("Old Regime : Allows deductions like 80C, 80D, Home Loan etc.")
        print("New Regime : Lower tax rates with limited deductions.")
        self.tax_regime = input("Tax Regime (old/new): ").strip().lower()

        print("\n" + "-" * 75)
        print("[Step 3] Income from Salary")
        print("-" * 75)
        print("Include:")
        print(" • Basic Pay")
        print(" • DA")
        print(" • Bonus")
        print(" • Incentives")
        print(" • Taxable Allowances")
        self.salary_income = float(input("Income from Salary (₹): "))

        print("\n" + "-" * 75)
        print("[Step 4] Income from Other Sources")
        print("-" * 75)
        print("Examples:")
        print(" • Freelancing")
        print(" • Rental Income")
        print(" • Dividend")
        print(" • Family Pension")
        self.other_income = float(input("Income from Other Sources (₹): "))

        print("\n" + "-" * 75)
        print("[Step 5] Interest Income")
        print("-" * 75)
        print("Include:")
        print(" • Savings Account Interest")
        print(" • Fixed Deposit Interest")
        print(" • Recurring Deposit Interest")
        self.bank_interest = float(input("Interest Income (₹): "))

        print("\n" + "-" * 75)
        print("[Step 6] Tax Already Paid")
        print("-" * 75)
        print("Enter total TDS deducted by Employer/Bank.")
        print("Refer Form-16 or Form-26AS.")
        self.tds_paid = float(input("TDS Paid (₹): "))

        print("\n✓ Input collection completed successfully.")

    def get_standard_deduction(self):

        print("\n[INFO] Determining Standard Deduction...")

        if self.tax_regime == "new":
            print("✓ New Regime Selected")
            print("✓ Standard Deduction = ₹75,000")
            return 75000
        else:
            print("✓ Old Regime Selected")
            print("✓ Standard Deduction = ₹50,000")
            return 50000

    def taxable_income(self):

        print("\n[INFO] Calculating Gross Income...")

        gross = (
            self.salary_income
            + self.other_income
            + self.bank_interest
        )

        print(f"Gross Income = ₹{gross:,.2f}")

        deduction = self.get_standard_deduction()

        taxable = max(0, gross - deduction)

        print(f"Taxable Income = Gross Income - Standard Deduction")
        print(f"Taxable Income = ₹{taxable:,.2f}")

        return taxable

    def calculate_tax(self, income):

        print("\n[INFO] Applying Income Tax Slabs...")

        tax = 0

        if self.tax_regime == "new":

            print("Using New Regime Slabs")

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

                    taxable_amount = limit - previous
                    slab_tax = taxable_amount * rate

                    print(f"₹{previous:,} - ₹{limit:,} @ {rate*100:.0f}% = ₹{slab_tax:,.2f}")

                    tax += slab_tax
                    previous = limit

                else:

                    taxable_amount = income - previous
                    slab_tax = taxable_amount * rate

                    print(f"₹{previous:,} - ₹{income:,} @ {rate*100:.0f}% = ₹{slab_tax:,.2f}")

                    tax += slab_tax
                    return max(0, tax)

            tax += (income - 2400000) * 0.30

        else:

            print("Using Old Regime Slabs")

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

        print(f"Income Tax = ₹{tax:,.2f}")

        return tax

    def print_summary(self):

        print("\n")
        print("=" * 75)
        print("                 PROCESSING TAX CALCULATION")
        print("=" * 75)

        taxable = self.taxable_income()

        tax = self.calculate_tax(taxable)

        print("\n[INFO] Adding Health & Education Cess @4%")

        cess = tax * 0.04

        total_tax = tax + cess

        print(f"Cess = ₹{cess:,.2f}")

        print("\n[INFO] Adjusting TDS Already Paid")

        balance = total_tax - self.tds_paid

        print("\n")
        print("=" * 75)
        print("                     INCOME TAX SUMMARY")
        print("=" * 75)

        print(f"Tax Regime                 : {self.tax_regime.title()}")
        print(f"Gross Income               : ₹{self.salary_income + self.other_income + self.bank_interest:,.2f}")
        print(f"Standard Deduction         : ₹{self.get_standard_deduction():,.2f}")
        print(f"Total Taxable Income       : ₹{taxable:,.2f}")
        print(f"Income Tax                : ₹{tax:,.2f}")
        print(f"Health & Education Cess   : ₹{cess:,.2f}")

        print("-" * 75)

        print(f"Total Tax Liability       : ₹{total_tax:,.2f}")
        print(f"TDS Already Paid          : ₹{self.tds_paid:,.2f}")

        print("-" * 75)

        if balance > 0:
            print(f"Outstanding Tax Payable   : ₹{balance:,.2f}")
            print("Refund Eligible          : ₹0.00")
        else:
            print("Outstanding Tax Payable  : ₹0.00")
            print(f"Refund Eligible          : ₹{-balance:,.2f}")

        print("=" * 75)

        print("\nIMPORTANT NOTES")
        print("-" * 75)
        print("✓ This is an estimated tax calculation.")
        print("✓ Verify your income using Form-16, AIS and Form-26AS.")
        print("✓ Employer TDS should match Form-26AS.")
        print("✓ FD Interest is taxable under 'Income from Other Sources'.")
        print("✓ Savings Account Interest may be eligible for deduction")
        print("  under Section 80TTA/80TTB (if applicable).")
        print("✓ This calculator currently considers only Standard Deduction.")
        print("✓ Deductions under Sections 80C, 80D, NPS, Home Loan,")
        print("  HRA, LTA, Capital Gains, and Surcharge are not included.")
        print("=" * 75)


if __name__ == "__main__":

    calculator = IncomeTaxCalculator()

    calculator.get_input()

    calculator.print_summary()
