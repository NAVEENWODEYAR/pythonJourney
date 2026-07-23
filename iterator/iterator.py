import unittest

# =====================================================
# ITERATION IN PYTHON - COMPLETE DEMONSTRATION
# =====================================================

# -----------------------------------------------------
# Functions
# -----------------------------------------------------

def iterate_for_loop(numbers):
    """Iterate through a list using a for loop."""
    result = []
    for num in numbers:
        result.append(num)
    return result


def iterate_iterator(data):
    """Iterate through a list manually using an iterator."""
    iterator_obj = iter(data)
    result = []

    while True:
        try:
            result.append(next(iterator_obj))
        except StopIteration:
            break

    return result


def internal_for_loop(values):
    """Simulates how a for loop works internally."""
    it = iter(values)
    result = []

    while True:
        try:
            result.append(next(it))
        except StopIteration:
            break

    return result


def iterate_string(text):
    """Iterate through a string."""
    result = []

    for ch in text:
        result.append(ch)

    return result


# =====================================================
# Demonstration
# =====================================================

def demo():
    # -------------------------------------------------
    # PART 1: FOR LOOP
    # -------------------------------------------------
    print("1. Iteration using for loop:")

    numbers = [10, 20, 30, 40, 50]

    for num in iterate_for_loop(numbers):
        print(num)

    print()

    # -------------------------------------------------
    # PART 2: ITERATOR
    # -------------------------------------------------
    print("2. Iteration using iterator:")

    data = ["A", "B", "C"]

    for item in iterate_iterator(data):
        print(item)

    print()

    # -------------------------------------------------
    # PART 3: INTERNAL WORKING
    # -------------------------------------------------
    print("3. Internal working of for loop (using iterator):")

    values = [1, 2, 3]

    for value in internal_for_loop(values):
        print(value)

    print()

    # -------------------------------------------------
    # PART 4: STRING ITERATION
    # -------------------------------------------------
    print("4. Iteration on string:")

    text = "HELLO"

    for ch in iterate_string(text):
        print(ch)


# =====================================================
# LeetCode-Style Unit Tests
# =====================================================

class TestIteration(unittest.TestCase):

    # -------------------------------------------------
    # FOR LOOP TESTS
    # -------------------------------------------------

    def test_for_loop_normal(self):
        self.assertEqual(
            iterate_for_loop([10, 20, 30]),
            [10, 20, 30]
        )

    def test_for_loop_empty(self):
        self.assertEqual(
            iterate_for_loop([]),
            []
        )

    def test_for_loop_single_element(self):
        self.assertEqual(
            iterate_for_loop([100]),
            [100]
        )

    # -------------------------------------------------
    # ITERATOR TESTS
    # -------------------------------------------------

    def test_iterator_normal(self):
        self.assertEqual(
            iterate_iterator(["A", "B", "C"]),
            ["A", "B", "C"]
        )

    def test_iterator_empty(self):
        self.assertEqual(
            iterate_iterator([]),
            []
        )

    def test_iterator_numbers(self):
        self.assertEqual(
            iterate_iterator([1, 2, 3]),
            [1, 2, 3]
        )

    # -------------------------------------------------
    # INTERNAL FOR LOOP TESTS
    # -------------------------------------------------

    def test_internal_for_loop(self):
        self.assertEqual(
            internal_for_loop([1, 2, 3]),
            [1, 2, 3]
        )

    def test_internal_for_loop_empty(self):
        self.assertEqual(
            internal_for_loop([]),
            []
        )

    # -------------------------------------------------
    # STRING ITERATION TESTS
    # -------------------------------------------------

    def test_string_iteration(self):
        self.assertEqual(
            iterate_string("HELLO"),
            ['H', 'E', 'L', 'L', 'O']
        )

    def test_string_empty(self):
        self.assertEqual(
            iterate_string(""),
            []
        )

    def test_string_single_character(self):
        self.assertEqual(
            iterate_string("A"),
            ['A']
        )

    def test_string_with_spaces(self):
        self.assertEqual(
            iterate_string("HI THERE"),
            ['H', 'I', ' ', 'T', 'H', 'E', 'R', 'E']
        )


# =====================================================
# Main
# =====================================================

if __name__ == "__main__":

    print("=" * 55)
    print("ITERATION DEMONSTRATION")
    print("=" * 55)

    demo()

    print("\n" + "=" * 55)
    print("RUNNING UNIT TESTS")
    print("=" * 55)

    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)