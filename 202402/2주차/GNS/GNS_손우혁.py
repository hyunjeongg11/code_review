# import sys
# sys.stdin = open("input.txt", "r")
 
t = int(input())
 
number = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
 
def findNumber(numStr):
    for i, num in enumerate(number):
        if num == numStr:
            return i
 
def solve(n, numStrList, tc):
    count = [0 for _ in range(10)]
    for num in numStrList:
        count[findNumber(num)] = count[findNumber(num)] + 1
    print(tc)
    cur = 0
    for i in range(10):
        while(1):
            if count[i] == 0:
                break
            print(number[i], end=" ")
            count[i] = count[i] - 1
    print()
 
for tc in range(t):
    tc, n = map(str, input().split())
    n = int(n)
    numStrList = input().split()
    solve(n, numStrList, tc)
