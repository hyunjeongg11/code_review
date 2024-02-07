import sys
sys.stdin = open('input.txt')

T = 10

for test in range(1, T+1):
    l = int(input())
    N = 8
    matrix = [list(map(str, input())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N-l+1):
            check = 0
            for k in range(l//2):
                if matrix[i][j+k] == matrix[i][j+l-1-k]:
                    check = check + 1
            if check == (l//2):
                cnt = cnt + 1
            check = 0
            for k in range(l//2):
                if matrix[j+k][i] == matrix[j+l-1-k][i]:
                    check = check + 1
            if check == (l//2):
                cnt = cnt + 1
    print(f'#{test} {cnt}')

# 슬라이싱이나 리버스로 다시 풀기