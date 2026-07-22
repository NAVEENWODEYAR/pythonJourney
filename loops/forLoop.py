# -----------------------------------------
# Python For Loop Demo Program
# -----------------------------------------
# A for loop is used to repeat a block
# of code a fixed number of times.
# -----------------------------------------

# Loop from 1 to 5
import unittest
def generate_numbers(start: int, end: int):
    """
    Returns a list of strings from start to end.
    Example:
    generate_numbers(1, 5)
    -> ['Number = 1', 'Number = 2', ..., 'Number = 5']
    """
    result = []

    for number in range(start, end + 1):
        result.append(f"Number = {number}")

    result.append("Loop finished!")
    return result


# -------------------------
# Unit Tests (LeetCode Style)
# -------------------------

class TestGenerateNumbers(unittest.TestCase):

    def test_example_case(self):
        expected = [
            "Number = 1",
            "Number = 2",
            "Number = 3",
            "Number = 4",
            "Number = 5",
            "Loop finished!"
        ]
        self.assertEqual(generate_numbers(1, 5), expected)

    def test_single_number(self):
        expected = [
            "Number = 3",
            "Loop finished!"
        ]
        self.assertEqual(generate_numbers(3, 3), expected)

    def test_empty_range(self):
        expected = [
            "Loop finished!"
        ]
        self.assertEqual(generate_numbers(5, 3), expected)

    def test_negative_numbers(self):
        expected = [
            "Number = -2",
            "Number = -1",
            "Number = 0",
            "Number = 1",
            "Number = 2",
            "Loop finished!"
        ]
        self.assertEqual(generate_numbers(-2, 2), expected)

    def test_large_range(self):
        result = generate_numbers(1, 100)

        self.assertEqual(result[0], "Number = 1")
        self.assertEqual(result[-2], "Number = 100")
        self.assertEqual(result[-1], "Loop finished!")
        self.assertEqual(len(result), 101)  # 100 numbers + final message


if __name__ == "__main__":
    unittest.main()