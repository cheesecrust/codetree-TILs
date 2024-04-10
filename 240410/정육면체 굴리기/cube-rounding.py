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
        dice = (left, numMap[ny][nx], front, back, bottom, top)
    #서 
    elif direction == 2:
        print(right)
        dice = (right, numMap[ny][nx], front, back, top, bottom)
    #북
    elif direction == 3:
        print(front)
        dice = (front, numMap[ny][nx], bottom, top, left, right)
    #남
    elif direction == 4:
        print(back)
        dice = (back, numMap[ny][nx], top, bottom, left, right)

    return (ny, nx, dice)
    
if __name__ == "__main__":
    n, m, x, y, k = map(int, input().split())
    numMap = [ list(map(int, input().split())) for _ in range(n)]
    roll = list(map(int, input().split()))

    top, bottom, front, back, left, right = 0, 0, 0, 0, 0, 0

    dice = (top, bottom, front, back, left, right)
    
    for direction in roll:
        y, x, dice = rolling(dice, y, x, direction)