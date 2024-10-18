#created by RaidenEi

from collections import deque

def doimau(M, N, magic, r, c, m, n):
    queue = deque([(r, c)])
    magic[r][c] = m
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < M and 0 <= ny < N and magic[nx][ny] == n:
                magic[nx][ny] = m
                queue.append((nx, ny))

M, N = map(int, input().split())
magic = []
for i in range(M):
    x = [int(i) for i in input().split()]
    magic.append(x)
r, c, m = map(int, input().split())
n = magic[r - 1][c - 1]
doimau(M, N, magic, r - 1, c - 1, m, n)

for i in range(M):
    for j in range(N):
        print(magic[i][j], end=' ')
    print()
