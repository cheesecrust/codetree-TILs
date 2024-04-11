gameMap = []
# 상 우상 우 우하 하 하좌 좌 좌상
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

class Rodolf:
    y, x = 0, 0

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return f'y {self.y}, x {self.x}'

    def compare(self, santa):
        return (santa.y - self.y) ** 2 + (santa.x - self.x) ** 2

    def distance(self, y, x):
        return (self.y - y) ** 2 + (self.x - x) ** 2

    # 상 우상 우 우하 하 하좌 좌 좌상
    # 0  1.  2 3   4  5.  6. 7
    def move(self, santa):
        if santa.y == self.y and santa.x > self.x: return 2
        elif santa.y == self.y and santa.x < self.x: return 6
        elif santa.y < self.y and santa.x == self.x: return 0
        elif santa.y > self.y and santa.x == self.x: return 4
        elif santa.y < self.y and santa.x < self.x: return 7
        elif santa.y > self.y and santa.x < self.x: return 5
        elif santa.y < self.y and santa.x > self.x: return 1 
        elif santa.y > self.y and santa.x > self.x: return 3
        else:
            print(self)
            print(santa)
            print("error")

class Santa:
    num = 0
    y, x = 0, 0
    score = 0
    stun = 0
    fail = False

    def __init__(self, num, y, x):
        self.y = y
        self.x = x
        self.num = num

    def __str__(self):
        return f'num {self.num}, y {self.y}, x {self.x}, score {self.score}, stun {self.stun}, fail {self.fail}'

    def compare(self, rodolf):
        return (rodolf.y - self.y) ** 2 + (rodolf.x - self.x) ** 2

def dfs(santa, direction):

    nxty = santa.y + dy[direction]
    nxtx = santa.x + dx[direction]

    # 밀려나면 탈락
    if nxty < 1 or nxty > N or nxtx < 1 or nxtx > N:
        santa.fail = True
        return

    santa.y = nxty
    santa.x = nxtx

    # 밀려난 곳에 산타가 있다.
    if gameMap[nxty][nxtx] != 0:
        nextNum = gameMap[nxty][nxtx]    
        nextSanta = santaList[nextNum]
        dfs(nextSanta, direction)
        
    gameMap[nxty][nxtx] = santa.num

def crush(santa, direction, amount, turn):
    gameMap[santa.y][santa.x] = 0

    santa.score += amount
    nxty = santa.y + dy[direction] * amount
    nxtx = santa.x + dx[direction] * amount

    if nxty < 1 or nxty > N or nxtx < 1 or nxtx > N:
        santa.fail = True
        return

    santa.stun = turn + 2

    santa.y = nxty
    santa.x = nxtx

    # 날아갔는데 산타가 존재, 상호작용 시작
    if gameMap[santa.y][santa.x] != 0:
        nextNum = gameMap[santa.y][santa.x]
        nextSanta = santaList[nextNum]
        dfs(nextSanta, direction)
        
    gameMap[santa.y][santa.x] = santa.num

def moveRodolf(turn):
    target = Santa(0,0,0)
    distance = 2147000000

    for santa in santaList[1:]:
        if santa.fail : continue

        tmp = santa.compare(rodolf)

        if tmp < distance:
            distance = tmp
            target = santa
        elif tmp == distance and target.y < santa.y:
            target = santa
        elif tmp == distance and target.y == santa.y and target.x < santa.x:
            target = santa

    # print("rodolf :", rodolf)
    # print("target :", target)

    direction = rodolf.move(target)

    # print("direction: ", direction)
    rodolf.y += dy[direction]
    rodolf.x += dx[direction]

    # 움직인 루돌프의 위치를 보고 충돌 판단
    if gameMap[rodolf.y][rodolf.x] != 0:
        # print("루돌프가 박음")
        nextNum = gameMap[rodolf.y][rodolf.x]
        nextSanta = santaList[nextNum]
        # print("nextSanta: ", nextSanta, nextNum)
        crush(nextSanta, direction, C, turn)

def moveSanta(turn):
    for santa in santaList[1:]:

        if santa.fail or santa.stun > turn:
            continue

        origin = rodolf.distance(santa.y, santa.x)
        direction = -1

        for i in range(0, 8, 2):
            nxty = santa.y + dy[i]
            nxtx = santa.x + dx[i]
            
            # 범위를 벗어남
            if(nxty < 1 or nxty > N or nxtx < 1 or nxtx > N): 
                continue

            # 이미 산타가 있음
            if gameMap[nxty][nxtx] != 0: 
                continue
            
            nxt = rodolf.distance(nxty, nxtx)

            # 멀어짐
            if(origin <= nxt): 
                continue

            # 가까워짐
            origin = nxt    
            direction = i

        if direction == -1:
            continue
        
        gameMap[santa.y][santa.x] = 0

        santa.y += dy[direction]
        santa.x += dx[direction]
        gameMap[santa.y][santa.x] = santa.num

        # 루돌프와 부딪힘
        if rodolf.compare(santa) == 0:
            # santa의 현재 좌표레서 충돌이 일어남
            crush(santa, (direction + 4) % 8, D, turn)

def calculateScore():
    cnt = 0
    for santa in santaList[1:]:
        if not santa.fail:
            santa.score += 1
        else:
            cnt += 1

    if cnt == len(santaList[1:]): 
        return False

    return True

def game(turn):
    moveRodolf(turn)
    moveSanta(turn)
    # print("aftet move rodolf: ",rodolf)
    # print(gameMap[1:])
    # print()
    return calculateScore()

if __name__ == "__main__":
    N, M, P, C, D = map(int, input().split())
    Ry, Rx = map(int, input().split())
    
    rodolf = Rodolf(Ry, Rx)
    santaList = [Santa(0, 0, 0) for _ in range(P + 1)]

    gameMap = [list(0 for _ in range(N+1)) for _ in range(N+1)]

    for i in range(P):
        a, b, c = map(int, input().split())
        santa = Santa(a, b, c)
        gameMap[b][c] = a
        santaList[a] = santa
    
    # print(gameMap[1:])
    # print()

    for i in range(1, M + 1):
        if not game(i): break
    
    for santa in santaList[1:]:
        print(santa.score, end = " ")