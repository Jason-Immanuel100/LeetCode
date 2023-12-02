def FizzBuzz(n):
    list = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0 and i != 0:
            list.append("FizzBuzz")
        elif i % 5 == 0 and i != 0:
            list.append("Buzz")
        elif i % 3 == 0 and i != 0:
            list.append("Fizz")
        else:
            list.append(str(i))
    return list

def test_FizzBuzz():
    assert FizzBuzz(3) == ["1","2","Fizz"]
    assert FizzBuzz(5) == ["1","2","Fizz","4","Buzz"]
    assert FizzBuzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

test_FizzBuzz()
print("Everything passed")  # This is a test to see if the function works properly
