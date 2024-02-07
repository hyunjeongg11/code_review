import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+ 1):
    N, M = map(str, input().split())
    num = list(map(str, input().split()))
    seq = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    clst = [0] * 10
    for i in range(int(M)):
        for j in range(10):
            if num[i] == seq[j]:
                clst[j] = clst[j] + 1
    print(N)
    for i in range(10):
        print((seq[i] + " ") * clst[i], end=" ")
    print() 