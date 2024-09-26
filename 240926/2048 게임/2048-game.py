import sys
input = sys.stdin.readline

# 오, 왼, 아, 위
dir = [0, 1, 2, 3]

N = 0
ori_board = [[] for _ in range(21)]
answer = 0

# 아래러
def move_down(board):
    copied = copy_board(board, N)

    for i in range(N - 1):
        for j in range(N):
            p = i
            while 0 <= p and copied[p][j] != 0 and copied[p + 1][j] == 0:
                copied[p][j], copied[p + 1][j] = copied[p + 1][j], copied[p][j]
                p -= 1

    for i in range(N - 1, 1, -1):
        for j in range(N):
            if copied[i][j] == copied[i - 1][j]:
                copied[i][j], copied[i - 1][j] = copied[i][j] + copied[i - 1][j], 0
                p = i
                while 2 <= p:
                    copied[p - 1][j], copied[p - 2][j] = copied[p - 2][j], copied[p - 1][j]
                    p -= 1

    return copied

def move_up(board):
    copied = copy_board(board, N)

    for i in range(N - 1, 0, -1):
        for j in range(N):
            p = i
            while p < N and copied[p][j] != 0 and copied[p - 1][j] == 0:
                copied[p][j], copied[p - 1][j] = copied[p - 1][j], copied[p][j]
                p += 1

    for i in range(N - 1):
        for j in range(N):
            if copied[i][j] == copied[i + 1][j]:
                copied[i][j], copied[i + 1][j] = copied[i][j] + copied[i + 1][j], 0
                p = i
                while p < N - 2:
                    copied[p + 1][j], copied[p + 2][j] = copied[p + 2][j], copied[p + 1][j]
                    p += 1

    return copied

def move_right(board):
    copied = copy_board(board, N)

    for i in range(N - 1):
        for j in range(N):
            p = i
            while 0 <= p and copied[j][p] != 0 and copied[j][p + 1] == 0:
                copied[j][p], copied[j][p + 1] = copied[j][p + 1], copied[j][p]
                p -= 1

    for i in range(N - 1, 1, -1):
        for j in range(N):
            if copied[j][i] == copied[j][i - 1]:
                copied[j][i], copied[j][i - 1] = copied[j][i] + copied[j][i - 1], 0
                p = i
                while 2 <= p:
                    copied[j][p - 1], copied[j][p - 2] = copied[j][p - 2], copied[j][p - 1]
                    p -= 1

    return copied

def move_left(board):
    copied = copy_board(board, N)
    
    for i in range(N - 1, 0, -1):
        for j in range(N):
            p = i
            while p < N and copied[j][p] != 0 and copied[j][p - 1] == 0:
                copied[j][p], copied[j][p - 1] = copied[j][p - 1], copied[j][p]
                p += 1

    for i in range(N - 1):
        for j in range(N):
            if copied[j][i] == copied[j][i + 1]:
                copied[j][i], copied[j][i + 1] = copied[j][i] + copied[j][i + 1], 0
                p = i
                while p < N - 2:
                    copied[j][p + 1], copied[j][p + 2] = copied[j][p + 2], copied[j][p + 1]
                    p += 1

    return copied

def find_max(board):
    result = 0

    for i in range(N):
        for j in range(N):
            if result < board[i][j]:
                result = board[i][j]

    return result

def copy_board(board, N):
    copied = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            copied[i][j] = board[i][j]
    return copied

def dfs(board, cnt):
    global answer
    if cnt == 5:
        tmp = find_max(board)
        if answer < tmp:
            answer = tmp
        return

    for i in dir:
        if i == 0:
            dfs(move_up(board), cnt + 1)
        elif i == 1:
            dfs(move_down(board), cnt + 1)
        elif i == 2:
            dfs(move_left(board), cnt + 1)
        elif i == 3:
            dfs(move_right(board), cnt + 1)

if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        ori_board[i] = list(map(int, input().split()))

    dfs(ori_board, 0)

    print(answer)