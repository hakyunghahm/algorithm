n = int(input())

coor = list(map(int, input().split()))

newcoor = sorted(set(coor))

# 각 숫자의 인덱스를 딕셔너리로 저장 
newcoordict = {value: idx for idx, value in enumerate(newcoor)}

result = [newcoordict[x] for x in coor]
print(' '.join(map(str, result)))