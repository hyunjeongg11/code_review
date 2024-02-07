import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):
    string = input()
    stack = [string[0]]
    for i in range(1, len(string)):
        if stack and stack[-1] == string[i]:
            stack.pop()
        else:
            stack.append(string[i])
    print(f'#{test} {len(stack)}') 