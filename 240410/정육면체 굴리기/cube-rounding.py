numMap = []
n, m = 0, 0

# 1 - 동, 2- 서, 3 - 북, 4 - 남

def rolling (dice, y, x, direction):
    dy = [0, 0, 0, -1, 1]
    dx = [0, 1, -1, 0, 0]

    top, bottom, front, back, left, right = dice

    ny, nx = y + dy[direction], x + dx[direction]

    if n <= ny or m <= nx or ny < 0 or nx < 0:
        return y, x, dice

    # 동
    if direction == 1:
        print(left)
        if numMap[ny][nx] == 0:
            numMap[ny][nx] = right
            dice = (left, right, front, back, bottom, top)
        else:
            dice = (left, numMap[ny][nx], front, back, bottom, top)
            numMap[ny][nx] = 0
    #서 
    elif direction == 2:
        print(right)
        if numMap[ny][nx] == 0:
            numMap[ny][nx] = left
            dice = (right, left, front, back, bottom, top)
        else:
            dice = (right, numMap[ny][nx], front, back, top, bottom)
            numMap[ny][nx] = 0
    #북
    elif direction == 3:
        print(front)
        if numMap[ny][nx] == 0:
            numMap[ny][nx] = back
            dice = (front, back, bottom, top, left, right)
        else:
            dice = (front, numMap[ny][nx], bottom, top, left, right)
            numMap[ny][nx] = 0
    #남
    elif direction == 4:
        print(back)

        if numMap[ny][nx] == 0:
            numMap[ny][nx] = front
            dice = (back, front, top, bottom, left, right)
        else:
            dice = (back, numMap[ny][nx], top, bottom, left, right)
            numMap[ny][nx] = 0

    return (ny, nx, dice)
    
if __name__ == "__main__":
    n, m, x, y, k = map(int, input().split())
    numMap = [ list(map(int, input().split())) for _ in range(n)]
    roll = list(map(int, input().split()))

    top, bottom, front, back, left, right = 0, 0, 0, 0, 0, 0

    dice = (top, bottom, front, back, left, right)
    
    for direction in roll:
        y, x, dice = rolling(dice, y, x, direction)