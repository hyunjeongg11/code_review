# import sys
# sys.stdin = open("input.txt", "r")
 
t = 10
 
def solve(n, arr, tc):
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            for k in range(n//2):
                if (arr[i][j+k] != arr[i][j-k+n-1]):
                    break
                if k == n//2 - 1:
                    cnt = cnt + 1
            for k in range(n // 2):
                if (arr[j+k][i] != arr[j-k+n-1][i]):
                    break
                if k == n//2 - 1:
                    cnt = cnt + 1
    print(f"#{tc} {cnt}")
 
for tc in range(t):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    solve(n, arr, tc+1)