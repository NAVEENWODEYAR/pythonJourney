class Solution:
    def predictIQ(self, dob: str, gender: str) -> int:
        """
        Demo function.
        This does NOT predict real IQ.
        It generates a deterministic pseudo-IQ based on the inputs.

        Parameters:
            dob: "YYYY-MM-DD"
            gender: "Male" or "Female"

        Returns:
            int: pseudo IQ between 85 and 115
        """
        seed = sum(ord(c) for c in (dob + gender))
        return 85 + (seed % 31)


# --------------------
# LeetCode-style tests
# --------------------

sol = Solution()

assert sol.predictIQ("1998-08-15", "Male") == 97
assert sol.predictIQ("2000-01-01", "Female") == 94
assert sol.predictIQ("1990-12-31", "Male") == 90
assert sol.predictIQ("1985-05-20", "Female") == 95
assert sol.predictIQ("2010-10-10", "Male") == 92

print("All test cases passed!")