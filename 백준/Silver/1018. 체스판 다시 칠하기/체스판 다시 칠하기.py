# 체스판 다시 칠하기 

n,m = map(int, input().split())

board = []
for _ in range(n):
    row = list(input())
    board.append(row)

def repaint(board, startrow, startcol):
    paint_w = 0
    paint_b = 0 
    
    for i in range(8):
        for j in range(8):
            current = board[startrow + i][startcol + j]
            
            if (i + j) % 2 == 0:
                if current != 'W':
                    paint_w += 1
                if current != 'B':
                    paint_b += 1
            else:  
                if current != 'B':
                    paint_w += 1
                if current != 'W':
                    paint_b += 1

    return min(paint_w, paint_b)
min_repaint = 2501
for i in range(n-7):
    for j in range(m-7):
          min_repaint = min(min_repaint,  repaint(board, i, j))


print(min_repaint)