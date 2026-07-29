# =====================================================
# LeetCode Style - Generator Example
# =====================================================

class Solution:
    def simple_generator(self):
        """
        Generator that yields numbers one by one.

        Returns:
            Generator[int, None, None]
        """
        yield 1
        yield 2
        yield 3


def run_test(test_case, expected):
    solution = Solution()

    # Convert generator output to list for comparison
    actual = list(solution.simple_generator())

    print("-" * 45)
    print(f"Test Case : {test_case}")
    print(f"Expected  : {expected}")
    print(f"Actual    : {actual}")

    if actual == expected:
        print("Result    : PASS")
    else:
        print("Result    : FAIL")


def main():

    # LeetCode Style Test Cases

    run_test(
        "Generator should yield [1, 2, 3]",
        [1, 2, 3]
    )

    run_test(
        "Generator length",
        [1, 2, 3]
    )

    run_test(
        "Generator values in order",
        [1, 2, 3]
    )

    # Demonstrating next()
    print("\nUsing next()")
    print("-" * 45)

    solution = Solution()
    gen = solution.simple_generator()

    print("First value :", next(gen))
    print("Second value:", next(gen))
    print("Third value :", next(gen))

    try:
        next(gen)
    except StopIteration:
        print("StopIteration raised after generator is exhausted.")


if __name__ == "__main__":
    main()
