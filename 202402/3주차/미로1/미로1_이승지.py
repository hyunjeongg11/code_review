# import sys
from collections import deque


# sys.stdin = open("input.txt", "r")


# 최단거리니까 bfs 썼어요
def bfs(s):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    dq = deque(s)
    while dq:
        # 앞에서 뺀당
        now = dq.popleft()
        visited[now[0]][now[1]] = 1

        for d in range(4):
            ni = now[0] + di[d]
            nj = now[1] + dj[d]

            if 0 <= ni < 16 and 0 <= nj < 16:
                # 도착점을 찾으면 1 반환
                if miro[ni][nj] == 3:
                    return 1
                elif miro[ni][nj] == 0 and visited[ni][nj] == 0:
                    dq.append([ni, nj])
    # 갈 수 있는 데로 다 갔는데도 못 찾았으면 0 반환
    return 0


for _ in range(1, 11):
    tc = int(input())
    miro = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    start = []
    for i in range(16):
        for j in range(16):
            # 시작점이면 ~
            if miro[i][j] == 2:
                start.append([i, j])
                break

    # bfs + 델타탐색
    print(f'#{tc} {bfs(start)}')
