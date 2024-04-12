# 위 오 아 왼
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

class Knight:
    row = 0
    col = 0
    height = 0
    width = 0
    heart = 0
    fail = False
    change = False
    totalHeart = 0

    def __init__(self, r=0, c=0, h=0, w=0, k = 0, num = 0):
        self.row = r        
        self.col = c

        self.height = h
        self.width = w
        self.heart = k
        self.num = num
        self.totalHeart = k

    def __str__(self):
        return f"row: {self.row}, col: {self.col}, heart: {self.heart}, totalHeart: {self.totalHeart}"

def changeMap(knight, num):
    row = knight.row
    col = knight.col
    height = knight.height
    width = knight.width

    for i in range(row, row + height):
        for j in range(col ,col + width):
            # 지도 표시시에는 음수로 기사번호 표시
            knightMap[i][j] = num

# 기사가 지정한 방향으로 한칸 이동한다.
def move(knight, direction, moveKnight):
    nxtRow = knight.row + dy[direction]
    nxtCol = knight.col + dx[direction]
    height = knight.height
    width = knight.width
    num = knight.num

    # 해당 방향으로 움직일 수 있는지
    # 이동한 곳 벽 있는지 check
    for i in range(nxtRow, nxtRow + height):
        for j in range(nxtCol, nxtCol + width):
            if i < 1 or j < 1 or i > L or j > L:
                return False

            if chessMap[i][j] == 2:
                return False
    
    # 내가 아닌 나이트가 있는지
    for i in range(nxtRow, nxtRow + height):
        for j in range(nxtCol, nxtCol + width):

            # 있다면 그 나이트 move
            if knightMap[i][j] != num and knightMap[i][j] != 0:
                nxtKnight = knightList[knightMap[i][j]]
                # 움직임이 실패하면 연쇄적으로 다 실패
                if not move(nxtKnight, direction, moveKnight): return False

    if not knight in moveKnight:
        moveKnight.append(knight)
    return True

def realMove(moveKnight, direction):
    for knight in moveKnight:
        # 원래 있던 자리 0으로 초기화
        changeMap(knight, 0)
        knight.change = True

    for knight in moveKnight:
        # 아무것도 없으면 이동
        knight.row += dy[direction]
        knight.col += dx[direction]
        # 다시 칠하기
        changeMap(knight, knight.num)

def changeHeart(knight):
    for i in range(knight.row, knight.row + knight.height):
        for j in range(knight.col, knight.col + knight.width):
            # 함정 밟음
            if chessMap[i][j] == 1:
                knight.heart -= 1

    # change가 끝남을 설정
    knight.change = False

    # 죽으면 맵 리셋
    if knight.heart <= 0:
        knight.fail = True
        changeMap(knight, 0)
            
def start():
    for order in orderList:
        knightNum, direction = order[0], order[1]
        knight = knightList[knightNum]

        if knight.fail: continue
        copyMap = [list(0 for _ in range(L + 1)) for _ in range(L + 1)]

        moveKnight = []
        # 움직임 실패
        if not move(knight, direction, moveKnight):
            continue
    
        # 움직임 성공   
        realMove(moveKnight, direction)

        # 밀린 후 체력 계산  
        # 명령으로 움직인 아이는 체력 변화가 없다.   
        knight.change = False 

        for curKnight in knightList[1:]:
            if curKnight.change: 
                changeHeart(curKnight)

if __name__ == "__main__":
    L, N, Q = map(int, input().split())

    # L * L
    # 1 부터 L 까지, map의 1은 함정, 2는 벽이다.
    chessMap = [list(0 for _ in range(L + 1))] + [[0] + list(map(int, input().split())) for _ in range(L)]
    
    # knight
    # r c h w k (r, c) 상단위치 h 높이, w 넓이, k 체력
    knightMap = [list(0 for _ in range(L + 1)) for _ in range(L + 1)]
    knightList = [Knight()]
    for i in range(1, N + 1):
        r, c, h, w, k = map(int, input().split())
        knight = Knight(r, c, h, w, k, i)

        # 기사 map에 채우기
        knightList.append(knight)
        changeMap(knight, knight.num)

    orderList = [ list(map(int, input().split())) for _ in range(Q)]

    start()

    # for i in range(1, N + 1): print(knightList[i])

    answer = 0
    for knight in knightList[1:]:
        if not knight.fail:
            answer += knight.totalHeart - knight.heart

    print(answer)