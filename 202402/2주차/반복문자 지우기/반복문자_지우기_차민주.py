# import sys
# sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):
    top = -1
    word = input()
    # size = len(word)
    stack = []
    for char in word:   # word 한 문자씩 순회하면서
        if top == -1:   # stack에 아무것도 없는 상태라면
            top += 1
            stack.append(char)
        else:   # stack이 빈 상태가 아니라면
            # 문자 비교하고 / push하거나 pop하거나
            if char != stack[top]:  # 해당 문자와 stack 맨 위의 문자가 다르면
                top += 1
                stack.append(char)
            else:   # 해당 문자와 stack 맨 위의 문자가 같으면
                top -= 1
                stack.pop() # stack에서 빼냄
    result = len(stack)

    print(f'#{test} {result}')
