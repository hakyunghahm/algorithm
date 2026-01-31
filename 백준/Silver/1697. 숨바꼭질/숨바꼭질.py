# 숨바꼭질 
from collections import deque

n,k = map(int, input().split())
max = 100001
visited = [0] * max 

def bfs(start):
    q = deque()
    q.append(start)
    
    while q:
        x = q.popleft()
        
        if x == k:
            print(visited[x])
            return
        
        for nx in [x+1, x-1, x*2]:
            if 0 <= nx < max and visited[nx]==0:
                visited[nx] = visited[x] + 1
                q.append(nx)

bfs(n)