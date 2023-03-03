#!/usr/bin/env python3
import sys

sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
from functools import lru_cache

import platform
if platform.python_implementation() == 'PyPy':
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

# def solve(N: int, M: int, S: List[str]) -> Tuple[List[str], str]:
def solve(N, M, S):
    INF = pow(10, 18)
    d1 = [INF] * N
    dN = [INF] * N
    d1[0] = 0
    dN[N-1] = 0

    for i in range(N):
        for k in range(1, M+1):
            if S[i][k-1] == '1':
                d1[i+k] = min(d1[i+k], d1[i] + 1)

            if S[N-1-i][k-1] == '1':
                dN[N-1-i] = min(dN[N-1-i+k] + 1, dN[N-1-i])
                
    ans = []
    for k in range(1, N-1):
        tmp = INF
        for i in range(M-1):
            s = k - i - 1
            for j in range(M):
                t = s + j + 1
                if 0 <= s < k and k < t < N and S[s][j] == '1':
                    tmp = min(tmp, d1[s] + dN[t] + 1)

        if tmp == INF:
            ans.append(-1)
        else:
            ans.append(tmp)

    print(*ans)
                



# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    S = [None for _ in range(N)]
    for i in range(N):
        S[i] = input()
    solve(N, M, S)


if __name__ == '__main__':
    main()
