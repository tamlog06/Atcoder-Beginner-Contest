#!/usr/bin/env python3
# from typing import *


# def solve(N: int, a: List[int]) -> int:
def solve(N, a):
    pass

def dfs(S, M, i):
    n_T = []
    n_S = []
    for s in S:
        if s >> i & 1:
            n_S.append(s)
        else:
            n_T.append(s)

    if len(n_S) == 0 or len(n_T) == 0:
        return M



# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    a = [None for _ in range(N)]
    for i in range(N):
        a[i] = int(next(tokens))
    assert next(tokens, None) is None
    a1 = solve(N, a)
    print(a1)


if __name__ == '__main__':
    main()
