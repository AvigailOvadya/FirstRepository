def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes(limit):
    """Calculate the sum of all prime numbers up to a given limit."""
    total = 0
    for num in range(2, limit + 1):
        if is_prime(num):
            total += num
    return total

# Example usage
limit = 20
print(f"The sum of prime numbers up to {limit} is: {sum_of_primes(limit)}")