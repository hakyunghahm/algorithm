# 요세푸스 문제 0
from collections import deque
n,k = map(int, input().split())
result = []
q = deque(range(1,n+1))

while q: 
    q.rotate(-(k-1))
    result.append(q.popleft())


print("<" + ", ".join(map(str,result)) + ">")