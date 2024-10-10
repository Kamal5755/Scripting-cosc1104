# Enter a prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# To check previous prime number
def find_previous_prime(num):
    for i in range(num - 1, 1, -1):
        if is_prime(i):
            return i
    return None

# To check next prime number

def find_next_prime(num):
    i = num + 1
    while True:
        if is_prime(i):
            return i
        i += 1

# to find divisor
def find_divisors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

# User input
def get_user_input():
    while True:
        try:
            user_input = int(input("Please enter a positive whole number: "))
            if user_input <= 0:
                print("That's not a positive number. Try again.")
            else:
                return user_input
        except ValueError:
            print("Invalid input! Please enter a valid positive whole number.")

def main():
    num = get_user_input()

    # Show the previous prime number
    previous_prime = find_previous_prime(num)
    if previous_prime:
        print(f"The prime number before {num} is {previous_prime}.")
    else:
        print(f"There is no prime number before {num}.")

    # Check if the number is prime
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
        print(f"Divisors of {num}: {find_divisors(num)}")

    # Show prime number
    next_prime = find_next_prime(num)
    print(f"The next prime number after {num} is {next_prime}.")

if __name__ == "__main__":
    main()
