# Program to calculate tax based on salary

class Solution:
    def calculateTax(self, salary: float) -> float:
        """
        Calculate income tax based on salary slabs.

        Slabs:
        - Up to 250000       : 0%
        - 250001 - 500000    : 5%
        - 500001 - 1000000   : 20%
        - Above 1000000      : 30%
        """

        if salary <= 250000:
            return 0.0
        elif salary <= 500000:
            return (salary - 250000) * 0.05
        elif salary <= 1000000:
            return (250000 * 0.05) + (salary - 500000) * 0.20
        else:
            return (250000 * 0.05) + (500000 * 0.20) + (salary - 1000000) * 0.30


# ----------------------------
# LeetCode-style Test Cases
# ----------------------------
def run_tests():
    solution = Solution()

    test_cases = [
        # (salary, expected_tax)
        (200000, 0.0),
        (250000, 0.0),
        (300000, 2500.0),
        (500000, 12500.0),
        (750000, 62500.0),
        (1000000, 112500.0),
        (1200000, 172500.0),
        (1500000, 262500.0),
    ]

    for i, (salary, expected) in enumerate(test_cases, 1):
        result = solution.calculateTax(salary)
        status = "PASS" if abs(result - expected) < 1e-6 else "FAIL"

        print(f"Test Case {i}:")
        print(f"Salary   = {salary}")
        print(f"Expected = {expected}")
        print(f"Output   = {result}")
        print(f"Result   = {status}")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()