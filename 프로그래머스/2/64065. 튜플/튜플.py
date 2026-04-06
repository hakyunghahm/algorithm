# 튜플

def solution(s): 
    # 바깥에 괄호 제거 
    #집합 하나씩 나눔 
    groups = s[2:-2].split("},{")
    
    #리스트로 바꿈 
    groups  = [list(map(int, group.split(","))) for group in groups]

    # 길이 기준 정렬
    groups.sort(key=len)

    answer = []
    used = set()

    for group in groups:
        for num in group:
            if num not in used:
                answer.append(num)
                used.add(num)

    return answer 
