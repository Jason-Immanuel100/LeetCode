def MaximumOddBinaryNumber(s):
    ones = ""
    zeros = ""
    for digit in s:
        if digit == "1":
            ones = ones + digit
        else:
            zeros = zeros + digit
    
    print(ones)
    print(zeros)

    maxbin = ""
    length = len(ones)
    new_ones = ""
    for i in range(1,length):
        new_ones = new_ones + "1"
    print(new_ones)
    max_bin = new_ones + zeros + "1"
    print(max_bin)
    return max_bin

import unittest

class TestMaximumOddBinaryNumber(unittest.TestCase):
    def test_maximum_odd_binary_number(self):
        self.assertEqual(MaximumOddBinaryNumber("1100"), "1001")
        self.assertEqual(MaximumOddBinaryNumber("1010"), "1001")
        self.assertEqual(MaximumOddBinaryNumber("1111"), "1111")
        self.assertEqual(MaximumOddBinaryNumber("0010"), "0001")
        self.assertEqual(MaximumOddBinaryNumber("1001"), "1001")

if __name__ == '__main__':
    unittest.main()


