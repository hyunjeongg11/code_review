import sys
sys.stdin = open('input.txt')
from collections import deque

# 상하좌우
dt_x = [0, 0, -1, 1]
dt_y = [-1, 1, 0, 0]

def bfs(x1, y1):  # 시작 좌표, 도착 좌표
    dq = deque()
    dq.append([x1, y1])
    visited = [[0] * 16 for _ in range(16)]  # visited 생성
    visited[x1][y1] = 1  # 시작점 방문 표시
    while dq:  # 처리 안된 정점이 남아있으면
        t = dq.popleft()  # 처리할 좌표
        for i in range(4):  # 4가지 방향에 대해서
            next_x = t[0] + dt_x[i]
            next_y = t[1] + dt_y[i]
            if (0 <= next_x < 16 and 0 <= next_y < 16) and data[next_x][next_y] != 1:  # 통로라면
                if visited[next_x][next_y] == 0:    # 방문하지 않았으면
                    dq.append([next_x, next_y])     # 인큐하고
                    visited[next_x][next_y] = 1     # 방문 처리
                    if data[next_x][next_y] == 3:
                        return 1
            else:
                continue  # 벽이라면 다음 반복문으로
    return 0  # G까지 경로가 없는 경우


for test in range(1, 11):
    N = int(input())
    data = [list(map(int, input())) for _ in range(16)]
    s_x, s_y = 0, 0
    for x in range(16):
        for y in range(16):
            if data[x][y] == 2:
                s_x, s_y = x, y  # 출발 좌표

    result = bfs(s_x, s_y)
    print(f'#{test} {result}')