# Problem 1. Two Sum
def twosum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

def test_twosum():
    assert twosum([2, 7, 11, 15], 9) == [2, 7], "Test case 1 failed"
    assert twosum([3, 2, 4], 6) == [2, 4], "Test case 2 failed"
    assert twosum([3, 3], 6) == [3, 3], "Test case 3 failed"

test_twosum()