#!/usr/bin/env python3
# from typing import *


# def solve(N: int, K: int) -> int:
def solve(N, K):
    for i in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            N = int(str(N) + '200')

    return N


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, K = map(int, input().split())
    a = solve(N, K)
    print(a)


if __name__ == '__main__':
    main()
