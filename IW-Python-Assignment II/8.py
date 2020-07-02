# 8. Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.


def check_prime(num):
    if num == 1:
        return False
    if num == 2:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
        else:
            return True


print(check_prime(24))


