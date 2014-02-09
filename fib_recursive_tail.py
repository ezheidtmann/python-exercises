def fib(N):
    return fib_helper(0, 1, N)

def fib_helper(current, next, n):
    """Tail recursive fibonnaci helper

    This function works from n = N to n = 0, working from fibonnaci sequence
    element 0 to element N. We begin with the 0th and 1st elements of the
    sequence while counting down from the target element of the sequence.

    In some languages, this tail recursion could be optimized by the compiler
    or runtime. I believe this optimization does not happen in Python,
    unfortunately.
    """

    if (n == 1): return next
    return fib_helper(next, current + next, n - 1)
