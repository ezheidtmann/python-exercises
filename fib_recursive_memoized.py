def fib(n):
    if (not hasattr(fib, 'known')):
        fib.known = [0, 1, 1]
        print "making list"

    if (len(fib.known) <= n or not fib.known[n]):
        print "%d: %s" % (n, str(fib.known))
        print "%d: computing %d" % (n, n)
        fib.known.insert(n, fib(n-2) + fib(n-1))
        print "%d: %s" % (n, str(fib.known))

    return fib.known[n]
