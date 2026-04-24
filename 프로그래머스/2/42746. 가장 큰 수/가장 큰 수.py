# 가장 큰 수

def solution(numbers):
    # 배열 안의 숫자들을 다 문자로 바꿔.
    str_numbers = [str(n) for n in numbers]
    # 배열 안의 숫자들을 가장 첫번째 자리를 비교해서 큰것부터 나열..
    # 첫번째 자리가 n으로 동일한 경우 그 다음자리 비교 (다음자리 없는건 nn)
    # 343434 333 303030 이렇게 세번씩 반복하면 결과 동일

    str_numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int("".join(str_numbers)))