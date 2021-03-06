#!/usr/bin/env python3
# from typing import *


# def solve(a: str, b: str, c: List[str], d: List[List[str]], e: str) -> int:
def solve(N, M, X, C, A):
    ans = -1
    for i in range(2**N):
        values = [0] * M
        money = 0
        for j in range(N):
            if (i >> j) & 1:
                for k in range(M):
                    values[k] += A[j][k]
                money += C[j]

        if all(values[k] >= X for k in range(M)):
            if ans == -1 or money < ans:
                ans = money
    return ans

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M, X = map(int, input().split())
    C = []
    A = []
    for i in range(N):
        q = list(map(int, input().split()))
        C.append(q[0])
        A.append(q[1:])

    a1 = solve(N, M, X, C, A)
    print(a1)


if __name__ == '__main__':
    main()
