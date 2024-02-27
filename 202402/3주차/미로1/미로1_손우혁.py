# import sys
# sys.stdin = open('input.txt')
 
from collections import deque
 
t = 10
 
path = '0'
wall = '1'
start = '2'
end = '3'
height = 16
width = 16
 
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
 
def findPoint():
    global startX, startY, endX, endY
    for i in range(height):
        for j in range(width):
            if maze[i][j] == start:
                startY = i
                startX = j
            if maze[i][j] == end:
                endY = i
                endX = j
 
def bfs(y, x):
    q = deque([[y, x]])
    visited[y][x] = 1
    while(q):
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if nx < 0 or ny < 0 or nx >= width or ny >= height:
                continue
            if visited[ny][nx] or maze[ny][nx] == wall:
                continue
            if maze[ny][nx] == end:
                visited[ny][nx] = 1
                return
            q.append([ny, nx])
            visited[ny][nx] = 1
 
def solve(tc):
    findPoint()
    bfs(startY, startX)
    print(f"#{tc} {visited[endY][endX]}")
 
for tc in range(t):
    input()
    startX = startY = endX = endY = -1
    maze = [input() for _ in range(height)]
    visited = [[0]*width for _ in range(height)]
    solve(tc+1)