# 나무 자르기 
n,m = map(int, input().split())

trees = list(map(int, input().split()))

# 조건을 만족하는 H 중에서 가장 큰 값 

start = 0
end = max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    treesum = sum((tree-mid) for tree in trees if tree>mid)
    if treesum >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)