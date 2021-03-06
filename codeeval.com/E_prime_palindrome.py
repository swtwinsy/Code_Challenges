def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

primes = prime_sieve(1000)

for p in primes[::-1]:
    if is_palindrome(p):
        print(p)
        break;
