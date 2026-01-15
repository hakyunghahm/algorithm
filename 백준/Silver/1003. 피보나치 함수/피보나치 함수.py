t = int(input())


for _ in range(t):
    n = int(input())
    def fibo(k):
        if k == 1: 
            return 0,1
        elif k == 0:
            return 1,0
        D = [0] * (k+1) # 0이 호출되는 횟수 
        M = [0] * (k+1) # 1이 호출되는 횟수 
        D[0] = 1
        D[1] = 0
        M[0] = 0
        M[1] = 1 
        for i in range(2,k+1):
            D[i] = D[i-1] + D[i-2]
            M[i] = M[i-1] + M[i-2]
        return D[k], M[k]    
    a, b = fibo(n)
    print(a,b, sep=" ")