# =====================================================
# ARRAYS (LISTS) IN PYTHON - DEMONSTRATION
# =====================================================

import unittest

# =====================================================
# ARRAYS (LISTS) IN PYTHON - DEMONSTRATION
# =====================================================

# -----------------------------------------------------
# Functions
# -----------------------------------------------------

def create_array():
    """Creates and returns the initial array."""
    return [10, 20, 30, 40, 50]


def get_element(arr, index):
    """Returns the element at the given index."""
    return arr[index]


def modify_element(arr, index, value):
    """Modifies an element at the given index."""
    arr[index] = value
    return arr


def traverse_array(arr):
    """Returns all elements as a list."""
    return [num for num in arr]


def add_element(arr, value):
    """Adds an element to the end of the array."""
    arr.append(value)
    return arr


def remove_element(arr, value):
    """Removes the first occurrence of the value."""
    arr.remove(value)
    return arr


def array_length(arr):
    """Returns the length of the array."""
    return len(arr)


# =====================================================
# Demonstration
# =====================================================

def demo():
    numbers = create_array()

    # 1. Accessing elements
    print("First element:", get_element(numbers, 0))
    print("Third element:", get_element(numbers, 2))

    # 2. Modifying elements
    modify_element(numbers, 1, 25)
    print("Updated array:", numbers)

    # 3. Traversing
    print("All elements in array:")
    for num in traverse_array(numbers):
        print(num)

    # 4. Adding elements
    add_element(numbers, 60)
    print("After adding 60:", numbers)

    # 5. Removing elements
    remove_element(numbers, 30)
    print("After removing 30:", numbers)

    # 6. Length
    print("Length of array:", array_length(numbers))


# =====================================================
# LeetCode-Style Unit Tests
# =====================================================

class TestArrayOperations(unittest.TestCase):

    def setUp(self):
        self.arr = create_array()

    # -------------------------
    # Test Create
    # -------------------------
    def test_create_array(self):
        self.assertEqual(self.arr, [10, 20, 30, 40, 50])

    # -------------------------
    # Test Access
    # -------------------------
    def test_access_first_element(self):
        self.assertEqual(get_element(self.arr, 0), 10)

    def test_access_middle_element(self):
        self.assertEqual(get_element(self.arr, 2), 30)

    def test_access_last_element(self):
        self.assertEqual(get_element(self.arr, 4), 50)

    def test_access_invalid_index(self):
        with self.assertRaises(IndexError):
            get_element(self.arr, 10)

    # -------------------------
    # Test Modify
    # -------------------------
    def test_modify_element(self):
        modify_element(self.arr, 1, 25)
        self.assertEqual(self.arr, [10, 25, 30, 40, 50])

    # -------------------------
    # Test Traverse
    # -------------------------
    def test_traverse_array(self):
        self.assertEqual(traverse_array(self.arr), [10, 20, 30, 40, 50])

    # -------------------------
    # Test Add
    # -------------------------
    def test_add_element(self):
        add_element(self.arr, 60)
        self.assertEqual(self.arr, [10, 20, 30, 40, 50, 60])

    def test_add_negative_number(self):
        add_element(self.arr, -5)
        self.assertEqual(self.arr[-1], -5)

    # -------------------------
    # Test Remove
    # -------------------------
    def test_remove_element(self):
        remove_element(self.arr, 30)
        self.assertEqual(self.arr, [10, 20, 40, 50])

    def test_remove_non_existing_element(self):
        with self.assertRaises(ValueError):
            remove_element(self.arr, 100)

    # -------------------------
    # Test Length
    # -------------------------
    def test_array_length(self):
        self.assertEqual(array_length(self.arr), 5)

    def test_length_after_add(self):
        add_element(self.arr, 60)
        self.assertEqual(array_length(self.arr), 6)

    def test_length_after_remove(self):
        remove_element(self.arr, 20)
        self.assertEqual(array_length(self.arr), 4)


# =====================================================
# Main
# =====================================================

if __name__ == "__main__":
    print("=" * 50)
    print("ARRAY DEMONSTRATION")
    print("=" * 50)
    demo()

    print("\n" + "=" * 50)
    print("RUNNING UNIT TESTS")
    print("=" * 50)

    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)