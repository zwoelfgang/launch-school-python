def factors(number):
    divisor = number
    result = []
    if number < 0:
        return result
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
