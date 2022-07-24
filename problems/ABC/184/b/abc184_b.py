#!/usr/bin/env python3
# from typing import *


# def solve(N: int, X: int, S: str) -> int:
def solve(N, X, S):
    ans = X
    for i in range(N):
        if S[i] == 'o':
            ans += 1
        else:
            ans = max(0, ans-1)
    return ans

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, X = map(int, input().split())
    S = input()
    a = solve(N, X, S)
    print(a)


if __name__ == '__main__':
    main()
