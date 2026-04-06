# 이차원 배열과 연산
from collections import Counter
r,c,k = map(int, input().split())

# 배열 입력받기 
A = []
for _ in range(3):
    row = list(map(int, input().split()))
    A.append(row)

# 한 행을 새로 만드는 함수 
def letssort(line):
    counter = Counter(line)
    
    if 0 in counter:
        del counter[0]
    
    newlines = list(counter.items())
    newlines.sort(key=lambda x:(x[1], x[0]))
    
    result = []
    for num, cnt in newlines:
        result.append(num)
        result.append(cnt)
        
    return result[:100]

# 전체 배열에 대한 R 연산 함수 
def goR(arr):
    newarr = []
    max_len = 0
    for line in arr:
        newline = letssort(line)
        newarr.append(newline)
        max_len = max(max_len, len(newline))
    max_len = min(max_len, 100)
    
    # 이제 max에 맞춰서 0을 채우거나, 자르자 
    for i in range(len(newarr)):
        newarr[i] = newarr[i][:100]
        newarr[i] += [0] * (max_len-len(newarr[i]))
    
    return newarr
# C 연산 함수 
def goC(arr):
    change = list(map(list, zip(*arr)))
    change = goR(change)
    return list(map(list, zip(*change)))


time = 0

while time <= 100:
    # 조건 만족 검사
    if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]) and A[r-1][c-1] == k:
        print(time)
        break
    if len(A) >= len(A[0]):
        A = goR(A)
    else:
        A = goC(A)
    
    time += 1
else: 
    print(-1)