# 깊은 복사를 위한 모듈
import copy

def find_painting_area(chess_board):
    
    count = 0
    
    for i in range(7):
        for j in range (7):
            
            # 현재 칸의 오른쪽 칸 확인
            if chess_board[i][j] == chess_board[i][j+1]:
                chess_board[i][j+1] = switch_block(chess_board[i][j+1])
                count = count + 1
            
            # 현재 칸의 밑에 칸 확인
            if chess_board[i][j] == chess_board[i+1][j]:
                chess_board[i+1][j] = switch_block(chess_board[i+1][j])
                count = count + 1

    # 마지막 칸 확인
    if chess_board[7][7] != chess_board[0][0]: 
        count = count + 1
        
    return count

def compare_chess_board(chess_board):
    
    # deepcopy를 이용한 깊은 복사
    first_chess_board = copy.deepcopy(chess_board)

    # 첫 번째 판의 시작 칸을 반전시킴 (흑 -> 백, 백->흑)
    second_chess_board = copy.deepcopy(chess_board)
    second_chess_board[0][0] = switch_block(second_chess_board[0][0])
    
    first_chess_board_count = find_painting_area(first_chess_board)
    
    # 리턴 시 second_chess_board_count가 더 작을 경우 + 1을 해줌 -> 개수를 찾기 전에 미리 하나 바꾸고 집어 넣었기 때문
    second_chess_board_count = find_painting_area(second_chess_board) + 1

    return first_chess_board_count if first_chess_board_count < second_chess_board_count else second_chess_board_count
    

# 흑 -> 백, 백 -> 흑
def switch_block(block):
    if block == "W":
        return "B"
    else :
        return "W"
    
# 행 열 값 입력력
row, col = list(map(int, input().split()))

chess_board = []
min = 99999

# 체스판 초기화
for i in range(row):
    chess_board.append(list(input()))

for i in range(row - 7):
    for j in range(col - 7):
        
        temp_chess_board = [row[j:8+j] for row in chess_board[i:8+i]]
        count_area = compare_chess_board(temp_chess_board)
        
        if min > count_area:
            min = count_area
            
print(min)