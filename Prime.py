def is_prime_number(n):
    """Returns True if n is prime, False otherwise"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

x = int(input("Enter the number of prime numbers you want to generate: "))
count = 0
n = 2

# loop until we have generated x prime numbers
while count < x:
    if is_prime_number(n):
        print(n)
        count += 1
    n += 1

# HEY HEY HEY HEY HEY I LUV U MUAH MUAH MUAH ... MUAH MUAH MUAH
# 123POGGERS456