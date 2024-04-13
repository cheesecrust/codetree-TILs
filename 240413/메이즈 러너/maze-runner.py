N, M, K = 0, 0, 0
maze = []
playerList = []
playerLocation = []
exitY, exitX = 0, 0

dy = [1,-1,0,0]
dx = [0,0,1,-1]

class Player:
    y = 0
    x = 0
    escape = False
    count = 0

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return f'y: {self.y}, x: {self.x}, escape: {self.escape}'
        
def move():
    for player in playerList:
        if player.escape:
            continue

        originDistance = abs(exitY - player.y) + abs(exitX - player.x)

        # -1은 움직이지 않는 상태
        moveDirection = -1
        for direction in range(4):
            nxtY = player.y + dy[direction]
            nxtX = player.x + dx[direction]
            
            # 범위 벗어나면 다시
            if nxtY < 1 or N < nxtY or nxtX < 1 or N < nxtX:
                continue   

            # 벽에 가로막히면 다시
            if maze[nxtY][nxtX] != 0:
                continue

            distance = abs(exitY - nxtY) + abs(exitX - nxtX)

            if distance < originDistance:
                moveDirection = direction
                originDistance = distance

        # 움직일 곳이 없다. 움직이지 않는다.
        if moveDirection == -1:
            continue

        #움직임 반영
        player.y += dy[moveDirection]
        player.x += dx[moveDirection]
        player.count += 1

        # 출구에 도착할시 탈출
        if player.y == exitY and player.x == exitX:
            player.escape = True

def findNearPlayer():
    leastDistance = 1000

    nearPlayerIdx = -1
    for i in range(len(playerList)):
        player = playerList[i]

        if player.escape:
            continue

        distance = abs(exitY - player.y) + abs(exitX - player.x)

        if distance < leastDistance:
            leastDistance = distance
            nearPlayerIdx = i

    if nearPlayerIdx == -1:
        print("error")

    return playerList[nearPlayerIdx]

def rotate90(pivotY, pivotX, length):
    global exitY, exitX

    newArr = [[0] * (N + 1) for _ in range(N + 1)]
    
    sy, sx = pivotY, pivotX 
    changeList = []
    for i in range(sy, sy + length +1):
        for j in range(sx, sx + length + 1):
            # 옮기는 대상이 벽이면 내구도 1 감소
            if maze[i][j] > 0:
                maze[i][j] -= 1

            oy, ox = i - sy, j - sx
            ry, rx = ox, length - oy
            newArr[ry][rx] = maze[i][j]
            
            # 옮기는 대상에 사람있으면 해당 사람 좌표 수정
            # j - sx + sy, length - (i - sy) + sx
            for player in playerList:
                if player.y == i and player.x == j:
                    changeList.append(player)

    for i in range(sy, sy + length + 1):
        for j in range(sx, sx + length + 1):
            maze[i][j] = newArr[i - sy][j - sx]
    
    for changePlayer in changeList:
        playerY = changePlayer.y
        playerX = changePlayer.x

        changePlayer.y = playerX - sx + sy
        changePlayer.x = length - (playerY - sy) + sx

    exitY, exitX = exitX - sx + sy, length - (exitY - sy) + sx

def rotate():
    nearPlayer = findNearPlayer()

    boxLength = max(abs(nearPlayer.y - exitY), abs(nearPlayer.x - exitX))
    pivotY, pivotX = 0, 0

    flag = False
    for i in range(exitY - boxLength, exitY + boxLength + 1):
        for j in range(exitX - boxLength, exitX + boxLength + 1):
            if i < 1 or i > N or j < 1 or j > N:
                continue

            for player in playerList:
                if player.escape: continue

                if i <= player.y <= i + boxLength and j <= player.x <= j + boxLength:
                    pivotY, pivotX = i, j
                    flag = True
                    break
    
            if flag:
                break

        if flag:
            break


    if pivotY == 0 and pivotX == 0:
        print("error")

    rotate90(pivotY, pivotX, boxLength)


def game():
    for i in range(K):
        # 참가자 움직이기
        move()

        # 모든 참가자가 탈출할경우
        for player in playerList:
            if not player.escape:
                break
        else:
            return

        # 미로 회전하기
        rotate()        

if __name__ == "__main__":
    N, M, K = map(int, input().split())

    maze = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

    inputList = [list(map(int, input().split())) for _ in range(M)]

    for i in range(len(inputList)):
        playerList.append(Player(inputList[i][0], inputList[i][1]))
    
    exitY, exitX = map(int,input().split())

    game()

    # 총 이동 수 계산
    cnt = 0
    for player in playerList:
        cnt += player.count

    # print(maze)
    # print(playerList[0])
    # print(playerList[1])
    # print(playerList[2])

    print(cnt)
    print(exitY, exitX)