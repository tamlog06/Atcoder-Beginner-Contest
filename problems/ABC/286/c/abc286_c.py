#!/usr/bin/env python3
# from typing import *


# def solve(N: int, A: int, B: int, S: str) -> int:
def solve(N, A, B, S):
    ans = float('inf')

    for i in range(N):
        tmp = A*i
        tmp_S = S[i:] + S[:i]

        for j in range(N//2):
            if tmp_S[j] != tmp_S[N-1-j]:
                tmp += B

        ans = min(ans, tmp)

    return ans




# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, A, B = map(int, input().split())
    S = input()
    a = solve(N, A, B, S)
    print(a)


if __name__ == '__main__':
    main()
