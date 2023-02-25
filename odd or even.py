num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

def is_prime(num):
    # A prime number is greater than 1
    if num <= 1:
        return False

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
