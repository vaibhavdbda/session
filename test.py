# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(number**0.5) + 1):  # Check divisors up to the square root of the number
        if number % i == 0:
            return False
    return True

# Input a number from the user
num = int(input("Enter a number to check if it's prime: "))

# Check and display the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
