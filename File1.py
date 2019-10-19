def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5))

print(factorial(5-1))
assert factorial(-25) == 1, "Failed"
print("first test passed")
assert factorial(-5) == 1, "Failed"
print ("second test passed")
assert factorial(10000) >= 1000
print("third test passed")


