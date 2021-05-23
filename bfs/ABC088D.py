from collections import deque

h, w = map(int, input().split())
maze = [list(input()) for i in range(h)]
sx, sy = 0, 0
gx, gy = h-1, w-1

def bfs():
    d = [[float("inf")]*w for i in range(h)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que = deque([])
    que.append((sx, sy))
    d[sx][sy] = 0

    while que:
        p = que.popleft()
        if p[0] == gx and p[1] == gy:
            break
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]

            if 0 <= nx < h and 0 <= ny < w and d[nx][ny] == float("inf") and maze[nx][ny] != "#":
                que.append((nx, ny))
                d[nx][ny] = d[p[0]][p[1]] + 1
    return d[gx][gy]

white = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            white += 1

num = bfs()
if num == float("inf"):
    print(-1)
else:
    print(white - num -1)