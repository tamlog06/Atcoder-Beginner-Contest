#!/usr/bin/env python3
# from typing import *


# def solve(N: int, S: List[str]) -> int:
def solve(N, S):
    initials = [0]*5

    for s in S:
        if s[0] in ['M', 'A', 'R', 'C', 'H']:
            initials['MARCH'.index(s[0])] += 1

    ans = 0
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                ans += initials[i] * initials[j] * initials[k]

    return ans

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    S = [None for _ in range(N)]
    for i in range(N):
        S[i] = input()
    a = solve(N, S)
    print(a)


if __name__ == '__main__':
    main()