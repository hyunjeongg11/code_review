import sys
sys.stdin = open('input.txt')

from collections import deque

T = 10
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    q = deque([[stR, stC]])
    visited[stR][stC] = 1

    while(q):
        curR, curC = q.popleft()
        for i in range(4):
            nextR, nextC = curR + dr[i], curC + dc[i]
            if 0 <= nextR < 16 and 0 <= nextC < 16:
                if visited[nextR][nextC] == 0 and maze[nextR][nextC] != 1:
                    if nextR == enR and nextC == enC:
                    # if maze[nextR][nextC] == 3:
                        visited[nextR][nextC] = 1
                        return
                    q.append([nextR, nextC])
                    visited[nextR][nextC] = 1


for test in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    visited = [[0]*16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                stR, stC = i, j
            if maze[i][j] == 3:
                enR, enC = i, j
    bfs()
    print(f'#{test} {visited[enR][enC]}')
