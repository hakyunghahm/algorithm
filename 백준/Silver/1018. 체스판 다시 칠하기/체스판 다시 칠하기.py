# 체스판 다시 칠하기 


# 브루트포스로 계속 움직이면서 
# 두종류의 체스판과 비교해서 repaint 수 구하기 

    

# 정답 출력 함수
def solution():
    n,m = map(int, input().split())
    
    board = []
    for _ in range(n):
        row = list(input())
        board.append(row)
    answer = 2501
    
    for start_row in range(0, n-7):
        for start_col in range(0, m-7):
            repaint = check(start_row, start_col, board)
            answer = min(answer, repaint)
   
    print(answer)
    
# 다시 칠해야 하는 색 개수 구하는 함수 
def check(start_row, start_col, board):
    # 해당 8x8을 체스판으로 만들때 필요한 최소 Repaint 수
    
    count = 0 # 틀린 칸 수 
    for i in range(0,8):
        for j in range(0,8):
            # 현재 칸 위치
            location = board[start_row + i][start_col + j]
            
            if (i+j) % 2 == 0:
                if location != "W":
                    count += 1
            else:
                if location != "B":
                    count += 1
    
    return min(count, 64-count)


solution()