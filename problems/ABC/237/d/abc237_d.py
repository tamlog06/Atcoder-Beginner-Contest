#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)


# def solve(N: int, S: str) -> Tuple[List[str], str]:
def solve(N, S):
    ans = str(N)
    for j in range(N-1, -1, -1):
        if S[j] == 'L':
            ans += str(j)
        else:
            ans = str(j) + ans

    return ans


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    S = input()
    a = solve(N, S)
    print(*a)


if __name__ == '__main__':
    main()