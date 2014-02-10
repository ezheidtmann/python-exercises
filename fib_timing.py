import fib_iterative
import fib_recursive
import fib_recursive_tail
import fib_recursive_memoized

import functools
from texttable import Texttable
from timeit import timeit

table = Texttable()

table.set_deco(Texttable.HEADER)
table.add_rows([[ 'n', 'fib(n)', 'method', 'time' ]])

def run_and_record_row(name, func, n):
    global table
    functor = functools.partial(func, n) 
    seconds = timeit(functor, number=100)
    table.add_row([ n, functor(), name, seconds ])

    
for n in range(5, 31):
    run_and_record_row('iterative', fib_iterative.fib, n)
    run_and_record_row('recursive', fib_recursive.fib, n)
    run_and_record_row('recursive_memoized', fib_recursive_memoized.fib, n)
    run_and_record_row('recursive_tail', fib_recursive_tail.fib, n)

print table.draw()
