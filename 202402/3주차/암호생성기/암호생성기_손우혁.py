# import sys
# sys.stdin = open('input.txt')
 
t = 10
 
def solve(pwdList, tc):
    cnt = 1
    while(1):
        temp = pwdList.pop(0)
        if temp - cnt <= 0:
            pwdList.append(0)
            break
        else:
            pwdList.append(temp - cnt)
            cnt = cnt % 5 + 1
    print(f"#{tc}", end=" ")
    print(*pwdList)
 
for _ in range(t):
    tc = int(input())
    pwdList = list(map(int, input().split()))
    solve(pwdList, tc)