# 연산자 끼워넣기 

n = int(input())
numbers = list(map(int, input().split()))
add, subtract, multiply, divide = map(int, input().split())

minresult = 1000000000
maxresult = -1000000000

# idx: 현재 몇번째 숫자까지 사용했는지 
# current: 지금까지 계산한 값 
def dfs (idx, current, add, subtract, multiply, divide):
    global minresult, maxresult
    
    if idx == n: 
        maxresult = max(maxresult, current)
        minresult = min(minresult, current)
        return
    
    # 덧셈
    if add > 0:
        dfs(idx + 1, current + numbers[idx], add - 1, subtract, multiply, divide)

    # 뺄셈
    if subtract > 0:
        dfs(idx + 1, current - numbers[idx], add, subtract - 1, multiply, divide)

    # 곱셈
    if multiply > 0:
        dfs(idx + 1, current * numbers[idx], add, subtract, multiply - 1, divide)

    # 나눗셈
    if divide > 0:
        if current < 0:
            dfs(idx + 1, -(-current // numbers[idx]), add, subtract, multiply, divide - 1)
        else:
            dfs(idx + 1, current // numbers[idx], add, subtract, multiply, divide - 1)

dfs(1, numbers[0], add, subtract, multiply, divide)

print(maxresult)
print(minresult)