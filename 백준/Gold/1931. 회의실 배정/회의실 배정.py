# 회의실 배정

n = int(input())
meetings = []
for _ in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
endtime = 0

for start, end in meetings:
    if start >= endtime:
        count += 1
        endtime = end

print(count)