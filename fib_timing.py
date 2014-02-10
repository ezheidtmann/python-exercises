import fib_iterative
import fib_recursive
import fib_recursive_tail
import fib_recursive_memoized

import functools, sys, StringIO
from texttable import Texttable
from timeit import timeit

table = Texttable()

table.set_deco(Texttable.HEADER)
table.add_rows([[ 'n', 'fib(n)', 'method', 'time' ]])

def run_and_record_row(name, func, n):
    if (not hasattr(run_and_record_row, 'too_long')):
        run_and_record_row.too_long = {}

    if name not in run_and_record_row.too_long:
        global table
        functor = functools.partial(func, n)
        seconds = timeit(functor, number=100)
        table.add_row([ n, functor(), name, seconds ])

        if seconds > 1:
            run_and_record_row.too_long[name] = True
            return False

ret = True

# Suppress output from called functions
orig_out = sys.stdout
sys.stdout = StringIO.StringIO()
for n in range(5, 700):
    ret = run_and_record_row('iterative', fib_iterative.fib, n) or ret
    ret = run_and_record_row('recursive', fib_recursive.fib, n) or ret
    ret = run_and_record_row('recursive_memoized', fib_recursive_memoized.fib, n) or ret
    ret = run_and_record_row('recursive_tail', fib_recursive_tail.fib, n) or ret

    if (not ret):
        break

# Restore regular output method
sys.stdout = orig_out

print table.draw()
