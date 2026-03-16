# 가장 긴 증가하는 부분 수열 

n = int(input())

numbers = list(map(int, input().split()))

# dp[n] = n번째 숫자까지 중에서 제일 긴 부분수열 길이 
dp = [0] * (n)

dp[0] = 1

for i in range(1, n):
    mx = 0 
    for j in range(i):
        if numbers[j] < numbers[i]:
            if dp[j] > mx:
                mx = dp[j]
    dp[i] = mx + 1
        

print(max(dp))