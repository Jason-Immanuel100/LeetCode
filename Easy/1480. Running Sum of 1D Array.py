def runningSum(nums):
    for i in range(len(nums)-1):
        nums[i+1] = nums[i] + nums[i+1]
    return nums

def test_runningSum():
    assert runningSum([1,2,3,4]) == [1,3,6,10]
    assert runningSum([1,1,1,1,1]) == [1,2,3,4,5]
    assert runningSum([3,1,2,10,1]) == [3,4,6,16,17]

if __name__ == "__main__":  
    test_runningSum()
    print("Everything passed")