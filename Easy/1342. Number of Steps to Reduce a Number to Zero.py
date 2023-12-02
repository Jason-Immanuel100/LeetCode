#Problem 1342. Number of Steps to Reduce a Number to Zero
def numberOfSteps(num):
    steps = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
            steps += 1
        else:
            num = num - 1
            steps += 1
    return steps

def test_numberOfSteps():
    assert numberOfSteps(14) == 6
    assert numberOfSteps(8) == 4
    assert numberOfSteps(123) == 12
    
if __name__ == "__main__":
    test_numberOfSteps()
    print("Everything passed")
