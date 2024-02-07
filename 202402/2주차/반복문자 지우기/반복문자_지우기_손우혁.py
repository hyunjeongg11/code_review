# import sys
# sys.stdin = open("input.txt", "r")
 
t = int(input())
 
def top(stack):
    return stack[-1]
 
def isEmpty(stack):
    if(len(stack) == 0):
        return True
    return False
 
def solve(line, tc):
    stack = []
 
    for char in line:
        if isEmpty(stack):
            stack.append(char)
        else:
            if top(stack) == char:
                stack.pop()
            else:
                stack.append(char)
 
    print(f"#{tc} {len(stack)}")
 
for tc in range(t):
    line = input()
    solve(line, tc+1)