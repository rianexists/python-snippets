def is_prime(num):
    result = True
    for i in range(2, num):
        if num % i == 0 and num != 2:
            result = False
    return result