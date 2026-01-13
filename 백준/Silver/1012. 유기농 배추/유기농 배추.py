# 유기농 배추

# 연결된 덩어리들이 몇개인가? 
import sys 
from collections import deque

input = sys.stdin.readline 



def solve(): 
    m,n,k = map(int, input().split())
    # 2차원 배추밭 초기화
    farm = [[0] * m for _ in range(n)]

    # 주어진 위치에 배추 심기 
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
        
    worm = 0
    visited = [[False]* m for _ in range(n)]

    def bfs(sy,sx):
        # 시작점 삽입 및 방문 처리 
        queue = deque([(sy, sx)])
        visited[sy][sx] = True
        
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        
        # 큐가 빌 때까지: 연결된 모든 배추를 찾을 때까지 
        while queue:
            # 큐의 가장 앞에 있는 좌표 꺼냄 
            y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                # 배추밭 범위 내에 있는지 확인
                if 0 <= ny < n and 0 <= nx < m:
                    # 배추가 있고(1) + 아직 방문하지 않았다면
                    if farm[ny][nx] == 1 and not visited[ny][nx]:
                        # 방문 표시를 하고 큐에 넣음
                        visited[ny][nx] = True
                        queue.append((ny, nx))
                        
                        
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                worm += 1
    print(worm)
    
    
t = int(input())
for _ in range(t):
    solve()