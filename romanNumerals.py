import unittest


# Goal
# Write a function that converts integers into roman numerals
# It is OK to reject integers > 3999

# Examples
# 1 - I
# 5 - V
# 10 - X
# 50 - L
# 100 - C
# 500 - D
# 1000 - M
# 1836 - MDCCCXXXVI
# 2499 - MMCDXCIX
# 3949 - MMMCMXLIX


class RomanNumeralsTestCases(unittest.TestCase):
    def test(self):
        # Given
        i_write_tests_first = True
        # When
        expected = i_write_tests_first
        actual = i_write_tests_first
        # Then
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
