#!/usr/bin/env python3
# from typing import *
import sys
sys.setrecursionlimit(10**6)
from functools import lru_cache
# from math import sqrt

def popcount(x):
    '''xの立っているビット数をカウントする関数
    (xは64bit整数)'''

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f # 8bitごと
    x = x + (x >> 8) # 16bitごと
    x = x + (x >> 16) # 32bitごと
    x = x + (x >> 32) # 64bitごと = 全部の合計
    return x & 0x0000007f

# 巡回セールスマン問題

# 頂点0からスタートして、全ての頂点を1回ずつ通って頂点0に戻る時の最短経路の長さを求める
# d: 隣接行列: d[i][j] = iからjへの距離
def TSP(d, N, M):
    # dp[S][v]: 集合Sに含まれる頂点をすべて通り、頂点vにいる時に、他の頂点を全て通って頂点0に戻る最短経路の長さ
    # ただし、Sは頂点0を含まない

    INF = pow(10, 18)
    dp = [[INF] * (N+M) for _ in range(1 << (N+M))]

    # 初期条件
    index = (1 << N) - 1
    for i in range(1 << M):
        dp[index | (i << N)][0] = 0

    for s in range((1 << (N+M)) - 1, -1, -1):
        # sの状態でvにいる時の最小値

        # 達成不可能
        # if popcount(s) - popcount(s >> N) == N-1 and s & 1:
        if s & 1 and popcount(s) - popcount(s >> N) < N:
            continue
        for v in range(N+M):
            # 次にuに移る
            for u in range(N+M):
                # uをまだ訪れていない場合
                if not (s >> u) & 1:
                    boost = popcount(s >> N)

                    # dp[s][v] = min(dp[s][v], dp[s | 1 << u][u] + d[v][u]/(1 << boost))
                    dp[s][v] = min(dp[s][v], dp[s | 1 << u][u] + d[v][u]/(pow(2, boost)))

    return dp[0][0]

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    X = [None for _ in range(N+1)]
    Y = [None for _ in range(N+1)]
    P = [None for _ in range(M)]
    Q = [None for _ in range(M)]
    X[0] = 0
    Y[0] = 0
    for i in range(1, N+1):
        X[i], Y[i] = map(int, input().split())
    for i in range(M):
        P[i], Q[i] = map(int, input().split())

    N += 1
    d = [[-1] * (N+M) for _ in range(N+M)]

    for i in range(N+M):
        for j in range(i, N+M):
            if i < N:
                a = (X[i], Y[i])
            else:
                a = (P[i-N], Q[i-N])
            if j < N:
                p = (X[j], Y[j])
            else:
                p = (P[j-N], Q[j-N])

            d[i][j] = ((a[0] - p[0]) ** 2 + (a[1] - p[1]) ** 2) ** 0.5
            d[j][i] = d[i][j]

    # return TSP(d, N, M)
    print(TSP(d, N, M))


main()
