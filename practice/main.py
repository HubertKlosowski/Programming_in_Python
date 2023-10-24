def sieve_of_eratosthenes(end):
    if type(end) is not int or end < 2:
        return [-1]
    arr = [i for i in range(2, end + 1)]
    boolean = [True for _ in range(2, end + 1)]
    for el in arr:
        for i in range(2 * el, end + 1, el):
            if i in arr:
                boolean[i - 2] = False
    primes = []
    for i, el in enumerate(boolean):
        if el is not False:
            primes.append(arr[i])
    return primes


def sieve_of_eratosthenes1(end):
    if type(end) is not int or end < 2:
        return [-1]
    arr = [i for i in range(2, end + 1)]
    for el in arr:
        for i in range(2 * el, end + 1, el):
            if i in arr:
                arr.remove(i)
    return arr


print(sieve_of_eratosthenes(100))
print(sieve_of_eratosthenes1(100))
