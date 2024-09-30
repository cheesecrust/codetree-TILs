import sys
input = sys.stdin.readline

N, M = 0, 0
board = [list() for _ in range(200)]

# 직선
def first():
    result = 0

    for i in range(N):
        for j in range(M):
            if j + 3 >= M :
                continue
            tmp = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j + 3]
            result = max(result, tmp)

    for i in range(N):
        if i + 3 >= N :
            continue
        for j in range(M):
            tmp = board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 3][j]
            result = max(result, tmp)

    return result

def second():
    result = 0

    for i in range(N):
        for j in range(M):
            if i + 1 >= N or j + 1 >= M:
                continue

            tmp = board[i][j] + board[i + 1][j] + board[i][j + 1] + board[i + 1][j + 1]
            result = max(result, tmp)

    return result
# L
def third():
    result = 0

    for i in range(N):
        for j in range(M):
            if i + 2 >= N or j + 1 >= M:
                continue
            tmp = board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 2][j + 1]
            result = max(result, tmp)

    for i in range(N):
        for j in range(M):
            if i - 1 < 0 or j + 2 >= M:
                continue
            tmp = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i - 1][j + 2]
            result = max(result, tmp)

    for i in range(N):
        for j in range(M):
            if i + 2 >= N or j + 1 >= M:
                continue
            tmp = board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1]
            result = max(result, tmp)

    for i in range(N):
        for j in range(M):
            if i + 1 >= N or j + 2 >= M:
                continue
            tmp = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j]
            result = max(result, tmp)

    return result

def fourth():
    result = 0

    for i in range(N):
        for j in range(M):
            if i + 1 >= N or j + 2 >= M:
                continue
            tmp = board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 1][j + 2]
            result = max(result, tmp)

    for i in range(N):
        for j in range(M):
            if i - 1 < 0 or j + 2 >= M:
                continue
            tmp = board[i][j] + board[i][j + 1] + board[i - 1][j + 1] + board[i - 1][j + 2]
            result = max(result, tmp)
    
    return result

def five():
    result = 0

    # ㅗ
    for i in range(N):
        for j in range(M):
            if i - 1 < 0 or j + 2 >= M:
                continue
            tmp = board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i - 1][j + 1]
            result = max(result, tmp)

    # ㅏ
    for i in range(N):
        for j in range(M):
            if i + 2 >= N or j + 1 >= M:
                continue
            tmp = board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j]
            result = max(result, tmp)

    # ㅜ
    for i in range(N):
        for j in range(M):
            if i + 1 >= N or j + 2 >= M:
                continue
            tmp = board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i][j + 2]
            result = max(result, tmp)

    # ㅓ
    for i in range(N):
        for j in range(M):
            if i + 2 >= N or j - 1 < 0:
                continue
            tmp = board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 1][j - 1]
            result = max(result, tmp)

    return result

if __name__ == "__main__":
    N, M = map(int, input().split())

    for i in range(N):
        board[i] = list(map(int, input().split()))

    answer = max(first(), second(), third(), fourth(), five())
    print(answer)