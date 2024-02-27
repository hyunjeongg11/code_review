def bfs(s_i,s_j,N):
    q = []  # 큐
    visited = [[0]*N for _ in range(N)]
    q.append((s_i,s_j)) # 시작점 인큐
    visited[s_i][s_j] = 1  # 시작점 방문표시

    dr = [-1, 0, 0, 1]
    dc = [0, 1, -1, 0]
    d = 0  # 0: 위, 1: 오, 2: 왼 3: 아래

    while q:    # 큐가 비워질때까지...(남은 정점이 있으면)
        end_i, end_j = q[0] # 처리할 정점
        # t에서 할일...
        if arr[end_i][end_j] == 3:
            return 1

        for k in range(4):
            ni = end_i + dr[k]
            nj = end_j + dc[k]

            if (ni>=0 and ni<N) and (nj>=0 and nj<N) and (visited[ni][nj] == 0) and (arr[ni][nj]!=1):
                q.append((ni, nj))
                visited[ni][nj] = 1 + visited[end_i][end_j]
                break
        else:
            q.pop(0)

    return 0 # G까지 경로가 없는 경우



for tc in range(1,11):
    T = int(input())
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_j = j
                start_i = i
                break

    result = bfs(start_i,start_j,N)

    print(f'#{tc} {result}')
