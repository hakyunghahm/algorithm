# 헌내기는 친구가 필요해 
from collections import deque
n,m = map(int, input().split())

campus = []
for _ in range(n):
    campus.append(list(input()))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]



def bfs(campus, sx, sy):
    person = 0
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = 1 
    
    while q: 
        x, y = q.popleft()
        if campus[x][y] == 'P':
            person += 1
        
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny <m:
                if visited[nx][ny] == 0 and campus[nx][ny] != 'X':
                    visited[nx][ny] =1 
                    q.append((nx, ny))
    return person 

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            sx, sy = i, j
            break

num = bfs(campus, sx, sy)
if num == 0:
    print("TT")
else:
    print(num)