from collections import deque

N, M = 0, 0
answer = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def copy_board(board):
    copied = [[0 for _ in range(8)] for _ in range(8)]

    for i in range(N):
        for j in range(M):
            copied[i][j] = board[i][j]
    
    return copied

def dfs(y, x, cnt, board):
    global answer

    if cnt == 3:
        tmp = copy_board(board)
        answer = max(answer, count(bfs(tmp)))
        return
    
    for i in range(x, M):
        if board[y][i] != 0:
            continue
        
        board[y][i] = 1
        dfs(y, i, cnt + 1, board)
        board[y][i] = 0

    for i in range(y + 1, N):
        for j in range(M):
            if board[i][j] != 0:
                continue
            
            board[i][j] = 1
            dfs(y, i, cnt + 1, board)
            board[i][j] = 0

    return

def bfs(board):
    q = deque()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                for k in range(4):
                    q.appendleft([i + dy[k], j + dx[k]])

    while(len(q) != 0):
        block = q.pop()
        y = block[0]
        x = block[1]

        if y < 0 or N <= y or x < 0 or M <= x:
            continue

        # 벽에 막힘 or 이미 불
        if board[y][x] == 1 or board[y][x] == 2:
            continue
        
        board[y][x] = 2
        for i in range(4):
            q.appendleft([y + dy[i], x + dx[i]])

    return board

def count(board):
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                answer += 1

    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list() for _ in range(8)]

    for i in range(N):
        board[i] = list(map(int, input().split()))

    dfs(0, 0, 0, board)

    print(answer)