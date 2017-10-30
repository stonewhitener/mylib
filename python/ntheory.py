def sieve(n):
    """
    Sieve of Eratosthenes
    """
    s = [True for _ in range(n + 1)]
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * 2, len(s), i):
                s[j] = False
    return (i for i in range(n + 1) if s[i] and i > 1)
