#!/usr/bin/env python3
# from typing import *
import sys
sys.setrecursionlimit(10**7)
from functools import lru_cache

MOD = 998244353


# def solve(N: int, K: int, A: List[int]) -> int:
# def solve(N, K, A):
    # A = sorted(list(set(A)))

    # n_count = [1]

    # count = 1
    # a = 0
    # n = 0

    # while True:
        # if a < len(A) and A[a] == n:
            # n_count.append(count)
            # a += 1
        # else:
            # count += 1
            # if count > K:
                # break
            # n_count.append(count)
        # n += 1


    # fact = [1, 1]
    # factinv = [1, 1]
    # inv = [0, 1]

    # n = len(n_count) + K

    # for i in range(2, n+1):
        # fact.append((fact[-1] * i) % MOD)
        # inv.append((-inv[MOD%i] * (MOD // i) % MOD))
        # factinv.append(((factinv[-1] * inv[-1]) % MOD))

    # def cmb(n, r, p):
        # if (r < 0) or n < r:
            # return 0

        # r = min(r, n-r)
        # return fact[n] * factinv[r] * factinv[n-r] % p

    # ans = 0
    # for i in range(len(n_count)):
        # nn = i+1
        # r = K - n_count[i]

        # ans += cmb(nn + r - 1, r, MOD)
        # ans %= MOD

    # return ans

def solve(N, K, A):
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]

    n = 5*10**5

    for i in range(2, n+1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((-inv[MOD%i] * (MOD // i) % MOD))
        factinv.append(((factinv[-1] * inv[-1]) % MOD))

    def cmb(n, r, p):
        if (r < 0) or n < r:
            return 0

        r = min(r, n-r)
        return fact[n] * factinv[r] * factinv[n-r] % p

    exi = [0] * 400001
    for a in A:
        exi[a] = 1

    need, ans = 1, 0
    for i in range(N+K+1):
        if need > K:
            break

        n = i+1
        r = K - need
        ans += cmb(n + r - 1, r, MOD)
        ans %= MOD

        if exi[i] == 0:
            need += 1

    return ans


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    K = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, K, A)
    print(a)


if __name__ == '__main__':
    main()
