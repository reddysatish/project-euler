"""
https://projecteuler.net/problem=2 .

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

import sys

sum = 0


def even_fibonacci_sum(max_limit, first=0, second=1):
    global sum
    new_number = first + second

    if new_number > max_limit:
        return

    if new_number % 2 == 0:
        sum += new_number

    even_fibonacci_sum(max_limit, first=second, second=new_number)


def main():
    if len(sys.argv) < 2:
        print "Usage: python problem_002.py <positive_integer>"
        return
    try:
        max_limit = int(sys.argv[1])
        if max_limit < 1:
            print 0
            return
    except ValueError:
        print "Usage: python problem_002.py <positive_integer>"
    else:
        even_fibonacci_sum(max_limit)
        print sum


if __name__ == "__main__":
    main()
