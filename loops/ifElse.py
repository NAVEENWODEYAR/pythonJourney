# Python Program to Demonstrate Lists

import unittest

def list_operations():
    """
    Demonstrates common list operations and returns
    the results after each operation.
    """
    
    # Creating a list
    fruits = ["Apple", "Banana", "Mango", "Orange"]

    result = {}

    # Original list
    result["original"] = fruits.copy()

    # Accessing elements
    result["first"] = fruits[0]
    result["last"] = fruits[-1]

    # Append
    fruits.append("Grapes")
    result["after_append"] = fruits.copy()

    # Insert
    fruits.insert(1, "Pineapple")
    result["after_insert"] = fruits.copy()

    # Remove
    fruits.remove("Banana")
    result["after_remove"] = fruits.copy()

    # Pop
    removed_item = fruits.pop()
    result["removed_item"] = removed_item
    result["after_pop"] = fruits.copy()

    # Update
    fruits[2] = "Kiwi"
    result["after_update"] = fruits.copy()

    # Length
    result["length"] = len(fruits)

    # Sort
    fruits.sort()
    result["after_sort"] = fruits.copy()

    # Reverse
    fruits.reverse()
    result["after_reverse"] = fruits.copy()

    # Membership
    result["contains_apple"] = "Apple" in fruits

    # Slice
    result["slice"] = fruits[:2]

    # Clear
    fruits.clear()
    result["after_clear"] = fruits.copy()

    return result


# -------------------------
# Unit Tests (LeetCode Style)
# -------------------------

class TestListOperations(unittest.TestCase):

    def setUp(self):
        self.result = list_operations()

    def test_original_list(self):
        self.assertEqual(
            self.result["original"],
            ["Apple", "Banana", "Mango", "Orange"]
        )

    def test_access_elements(self):
        self.assertEqual(self.result["first"], "Apple")
        self.assertEqual(self.result["last"], "Orange")

    def test_append(self):
        self.assertIn("Grapes", self.result["after_append"])

    def test_insert(self):
        self.assertEqual(self.result["after_insert"][1], "Pineapple")

    def test_remove(self):
        self.assertNotIn("Banana", self.result["after_remove"])

    def test_pop(self):
        self.assertEqual(self.result["removed_item"], "Grapes")
        self.assertNotIn("Grapes", self.result["after_pop"])

    def test_update(self):
        self.assertEqual(self.result["after_update"][2], "Kiwi")

    def test_length(self):
        self.assertEqual(self.result["length"], 5)

    def test_sort(self):
        self.assertEqual(
            self.result["after_sort"],
            ["Apple", "Kiwi", "Mango", "Orange", "Pineapple"]
        )

    def test_reverse(self):
        self.assertEqual(
            self.result["after_reverse"],
            ["Pineapple", "Orange", "Mango", "Kiwi", "Apple"]
        )

    def test_membership(self):
        self.assertTrue(self.result["contains_apple"])

    def test_slice(self):
        self.assertEqual(
            self.result["slice"],
            ["Pineapple", "Orange"]
        )

    def test_clear(self):
        self.assertEqual(self.result["after_clear"], [])


if __name__ == "__main__":
    unittest.main()