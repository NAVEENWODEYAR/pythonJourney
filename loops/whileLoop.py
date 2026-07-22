# -----------------------------------------
# Python While Loop Demo Program
# -----------------------------------------
# A while loop repeats a block of code
# as long as the condition is True.
# -----------------------------------------

import unittest


def generate_counts(limit: int):
    """
    Returns a list of strings from 1 to limit using a while loop.
    Example:
    generate_counts(5)
    -> ['Count = 1', 'Count = 2', ..., 'Count = 5', 'Loop finished!']
    """
    result = []
    count = 1

    while count <= limit:
        result.append(f"Count = {count}")
        count += 1

    result.append("Loop finished!")
    return result


# -------------------------
# Unit Tests (LeetCode Style)
# -------------------------

class TestGenerateCounts(unittest.TestCase):

    def test_example_case(self):
        expected = [
            "Count = 1",
            "Count = 2",
            "Count = 3",
            "Count = 4",
            "Count = 5",
            "Loop finished!"
        ]
        self.assertEqual(generate_counts(5), expected)

    def test_single_iteration(self):
        expected = [
            "Count = 1",
            "Loop finished!"
        ]
        self.assertEqual(generate_counts(1), expected)

    def test_zero_limit(self):
        expected = [
            "Loop finished!"
        ]
        self.assertEqual(generate_counts(0), expected)

    def test_negative_limit(self):
        expected = [
            "Loop finished!"
        ]
        self.assertEqual(generate_counts(-3), expected)

    def test_large_limit(self):
        result = generate_counts(100)

        self.assertEqual(result[0], "Count = 1")
        self.assertEqual(result[-2], "Count = 100")
        self.assertEqual(result[-1], "Loop finished!")
        self.assertEqual(len(result), 101)  # 100 counts + final message


if __name__ == "__main__":
    unittest.main()