chart = [list() for _ in range(15)]
N = 0
answer = 0

def dfs(start, pay):
    global answer

    if start > N:
        return

    if start == N:
        answer = max(answer, pay)
        return
    
    for i in range(start, N):
        dfs(start + (i - start) + chart[i][0], pay + chart[i][1])

    answer = max(answer, pay)
    return

if __name__ == "__main__":
    N = int(input())

    for i in range(N):
        chart[i] = list(map(int, input().split()))

    dfs(0, 0)
    print(answer)