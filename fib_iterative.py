def fib(n):
    if (n == 1 or n == 2): return 1

    current = 1
    prev = 1
    new = 0

    for i in range(2, n+1):
        if (i == n): return current

        new = current + prev
        prev = current
        current = new
