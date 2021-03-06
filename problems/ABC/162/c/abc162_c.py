#!/usr/bin/env python3
# from typing import *
from itertools import combinations_with_replacement
from functools import reduce
import math

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

# def solve(K: int) -> int:
def solve(K):
    l = [i for i in range(1, K+1)]
    c = combinations_with_replacement(l, 3)
    ans = 0
    for v in c:
        print(v)
        print(combinations_with_replacement(v, 3))
        ans += my_gcd(*v)
    return ans



# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    K = int(input())
    a = solve(K)
    print(a)


if __name__ == '__main__':
    main()
