import unittest

def sortedSquares(nums):
    list = []
    for num in nums:
        list.append(num**2)
    return sorted(list)

class TestSortedSquares(unittest.TestCase):
    def test_sorted_squares(self):
        self.assertEqual(sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])
        self.assertEqual(sortedSquares([0,2,3,4]), [0,4,9,16])
        self.assertEqual(sortedSquares([-5,-3,-1]), [1,9,25])

if __name__ == '__main__':
    unittest.main()