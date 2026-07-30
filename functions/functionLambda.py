# =====================================================
# LAMBDA FUNCTION - LEETCODE STYLE TEST CASES
# =====================================================

# Problem 1: Square of a number
def square(x):
    return x * x


# Problem 2: Add two numbers
def add(a, b):
    return a + b


# Problem 3: Find squares of numbers using map()
def get_squares(numbers):
    return list(map(lambda x: x * x, numbers))


# Problem 4: Filter even numbers
def get_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


# Problem 5: Sort students by marks
def sort_students(students):
    return sorted(students, key=lambda student: student[1])


# =====================================================
# TEST CASES
# =====================================================

def run_tests():

    # Test Case 1: Square function
    assert square(5) == 25
    assert square(10) == 100
    assert square(-3) == 9
    print("Square tests passed ✅")


    # Test Case 2: Addition function
    assert add(10, 20) == 30
    assert add(-5, 5) == 0
    assert add(0, 0) == 0
    print("Addition tests passed ✅")


    # Test Case 3: Map - Squares
    assert get_squares([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
    assert get_squares([]) == []
    assert get_squares([-1, -2]) == [1, 4]
    print("Map tests passed ✅")


    # Test Case 4: Filter - Even numbers
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert get_even_numbers([1, 3, 5]) == []
    assert get_even_numbers([]) == []
    print("Filter tests passed ✅")


    # Test Case 5: Sorting students
    students1 = [
        ("John", 80),
        ("Alice", 95),
        ("Bob", 70)
    ]

    assert sort_students(students1) == [
        ("Bob", 70),
        ("John", 80),
        ("Alice", 95)
    ]

    students2 = [
        ("Tom", 50),
        ("Jerry", 50)
    ]

    assert sort_students(students2) == [
        ("Tom", 50),
        ("Jerry", 50)
    ]

    print("Sorting tests passed ✅")


    print("\nAll test cases passed 🎉")


# Run all tests
run_tests()



4th floor, Brigade IRV Center, 
401, Nallurhalli Rd, 
Nallurhalli,
 Whitefield, Bengaluru, Karnataka 560066