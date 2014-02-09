def fib(n):
    print 'fib(%d)' % n
    if (not hasattr(fib, 'known')):
        fib.known = [1, 1, 1]
        print "making list"

    if (len(fib.known) <= n or not fib.known[n]):
        print "computing %d" % n
        fib.known.insert(n, fib(n-2) + fib(n-1))

    return fib.known[n]
