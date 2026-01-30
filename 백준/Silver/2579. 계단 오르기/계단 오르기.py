n = int(input())

stairs = []
for _ in range(n):
    stairs.append(int(input()))

dp = [0] * n

dp[0] = stairs[0]
if n > 1:
    dp[1] = stairs[0] + stairs[1]
if n > 2:
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3,n):
    dp[i] = max(dp[i-2], stairs[i-1]+dp[i-3]) + stairs[i]

print(dp[n-1])