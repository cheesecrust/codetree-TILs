from collections import deque

def getCandyMap():
    N, M = map(int, input().split())

    graph = [list(map(str, input())) for _ in range(N)]
    Ry, Rx, By, Bx = 0, 0, 0, 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'R':
                graph[i][j] = '.'
                Ry, Rx = i, j

            elif graph[i][j] == 'B':
                graph[i][j] = '.'
                By, Bx = i, j

    return graph, Ry, Rx, By, Bx


def gravity(Red, Blue, direction):

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    Ry, Rx = Red
    By, Bx = Blue
    
    result = 0

    other = False

    while True:
        Rny, Rnx = Ry + dy[direction], Rx + dx[direction]
        
        if graph[Rny][Rnx] == ".":
            if (Rny, Rnx) == Blue:
                other = True
            Ry, Rx = Rny, Rnx
        elif graph[Rny][Rnx] == "#":
            if other:
                Ry, Rx = Ry - dy[direction], Rx - dx[direction]
            break            
        else:
            result = 1
            break

    other = False
    while True:
        Bny, Bnx = By + dy[direction], Bx + dx[direction]

        if graph[Bny][Bnx] == ".":
            if (Bny, Bnx) == Red:
                other = True

            By, Bx = Bny, Bnx
        elif graph[Bny][Bnx] == "#":
            if other:
                By, Bx = By - dy[direction], Bx - dx[direction]
            break
        else:
            result = -1
            break

    return (Ry, Rx), (By, Bx), result

if __name__ == "__main__":
    graph, Ry, Rx, By, Bx = getCandyMap()
    
    Red = (Ry, Rx)
    Blue = (By, Bx)

    queue = deque([(Red, Blue, 0)])

    flag = False
    while queue:
        r, b, turn = queue.popleft()

        if turn == 10:
            continue

        for i in range(4):
            nRed, nBlue, check = gravity(r, b, i)

            if check == 1:
                print(turn + 1)
                flag =True
                break
            elif check == 0:
                queue.append((nRed, nBlue, turn + 1))

        if flag: break
    else:
        print(-1)