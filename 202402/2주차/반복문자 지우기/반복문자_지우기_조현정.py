import sys
sys.stdin = open('input.txt')

T = int(input())

def repeat(string, stack):
    stack.append(string[0])
    for i in range(1, len(string)):
        if stack and stack[-1] == string[i]:
            stack.pop()
        else:
            stack.append(string[i])
    return len(stack)


for test in range(1, T+1):
    string = list(input())
    stack = []
    ans = repeat(string, stack)
    print(f'#{test} {ans}')