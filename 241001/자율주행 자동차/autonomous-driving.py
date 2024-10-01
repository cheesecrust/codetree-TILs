N, M = 0, 0
y, x, d = 0, 0, 0
board = [list() for _ in range(51)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def move(y, x, d, answer):

    nxt_dir, nxt_y, nxt_x = 0, 0, 0

    for i in range(4):
        nxt_dir = (d + 1 + i) % 4

        nxt_y = y + dy[nxt_dir]
        nxt_x = x + dx[nxt_dir]

        if nxt_y < 0 or nxt_y >= N or nxt_x < 0 or nxt_x >= M:
            continue

        if board[nxt_y][nxt_x] != 0:
            continue
        break
        
    if board[nxt_y][nxt_x] != 0:
        nxt_y = y + dy[(d + 2) % 4]
        nxt_x = x + dx[(d + 2) % 4]
        # print("back,", nxt_y, nxt_x, d)

        if board[nxt_y][nxt_x] == 1:
            return answer
        
        return move(nxt_y, nxt_x, d, answer)
    
    # 성공
    board[nxt_y][nxt_x] = 2

    # for i in range(N):
    #     print(board[i])

    # print()

    return move(nxt_y, nxt_x, nxt_dir, answer + 1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    y, x, d = map(int, input().split())

    for i in range(N):
        board[i] = list(map(int, input().split()))
    
    board[y][x] = 2
    print(move(y, x, d, 1))