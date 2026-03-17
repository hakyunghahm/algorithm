# 평범한 배낭 

n, k = map(int, input().split())

items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w,v))


# dp[k] = 최대 무게가 k일 때 얻을 수 있는 최대 가치 
dp = [0] * (k+1)

# 물건을 하나씩 바꿔가면서 max(현재 물건을 안넣기-이 물건을 고려하기 전 그대로, 넣기-갱신)

# dp[j-w]는 아직 이 물건을 고려 안한 상태여야 하므로, 더 늦게 업데이트 해야함. 
# 고로 높은데부터 업데이트 해야함... 

# 물건을 바꿔가면서 dp를 계속 업데이트하는 거니까 items를 밖에 둬야함..
for w,v in items:
    for j in range(k, w-1, -1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[k])