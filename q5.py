def check_divisibility(num, divisor):
    # both num and divisor must be numeric
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return -1

    if divisor == 0:
        return -1

    # return True if num is divisible by divisor, otherwise return False
    if num % divisor == 0:
        return True
    else:
        return False


result1 = check_divisibility(10, 2)
print("Result 1:", result1)  # Output: True

result2 = check_divisibility(7, 3)
print("Result 2:", result2)  # Output: False
