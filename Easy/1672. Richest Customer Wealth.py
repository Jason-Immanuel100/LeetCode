# Problem: 1672. Richest Customer Wealth
def maximumWealth(accounts):
    max_value = sum(accounts[0])

    for i in range(len(accounts)):
        current_sum = sum(accounts[i])
        if current_sum > max_value:
            max_value = current_sum
    return max_value

def test_max_wealth():
    assert maximumWealth([[1,2,3],[3,2,1]]) == 6
    assert maximumWealth([[1,5],[7,3],[3,5]]) == 10
    assert maximumWealth([[2,8,7],[7,1,3],[1,9,5]]) == 17
    assert maximumWealth([[1,2,3],[3,2,1],[1,3,6]]) == 10
    assert maximumWealth([[1]]) == 1

if __name__ == "__main__":
    test_max_wealth()
    print("Everything passed")