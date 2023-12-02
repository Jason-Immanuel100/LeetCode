# Problem 217. Contains Duplicate

def contains_duplicate(nums):
    sets = set(nums)
    if len(sets) == len(nums):
        return False
    else:
        return True

def test_contains_duplicate():
    assert contains_duplicate([1,2,3,4,5]) == False, "Test case 1 failed"
    assert contains_duplicate([1,1,2,3,4]) == True, "Test case 2 failed"
    assert contains_duplicate([]) == False, "Test case 3 failed"
    assert contains_duplicate([1]) == False, "Test case 4 failed"
    assert contains_duplicate([1,1]) == True, "Test case 5 failed"
    assert contains_duplicate([1,2,3,4,5,5]) == True, "Test case 6 failed"

test_contains_duplicate()

