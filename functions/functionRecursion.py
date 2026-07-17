# =====================================================
# RECURSION PROGRAM - FACTORIAL OF A NUMBER
# =====================================================

class Solution:
    """
    Calculates the factorial of a number using recursion.
    """

    def factorial(self, n: int) -> int:
        """
        Returns the factorial of n.

        Base Case:
            0! = 1
            1! = 1

        Recursive Case:
            n! = n * (n - 1)!
        """

        # Base condition to stop recursion
        if n == 0 or n == 1:
            return 1

        # Recursive call
        return n * self.factorial(n - 1)


# =====================================================
# TEST CASES
# =====================================================

def run_tests():
    solution = Solution()

    # Test cases in the format:
    # (input, expected_output)
    test_cases = [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (5, 120),
        (6, 720),
        (8, 40320),
        (10, 3628800)
    ]

    passed = 0

    # Execute each test case
    for i, (num, expected) in enumerate(test_cases, start=1):

        # Get the actual result
        actual = solution.factorial(num)

        # Compare expected and actual output
        if actual == expected:
            print(f"Test Case {i} PASSED")
            passed += 1
        else:
            print(f"Test Case {i} FAILED")
            print(f"Input    : {num}")
            print(f"Expected : {expected}")
            print(f"Actual   : {actual}")

    # Display summary
    print("\n--------------------------------")
    print(f"Passed {passed} out of {len(test_cases)} test cases.")
    print("--------------------------------")


# =====================================================
# DRIVER CODE
# =====================================================

if __name__ == "__main__":
    run_tests()