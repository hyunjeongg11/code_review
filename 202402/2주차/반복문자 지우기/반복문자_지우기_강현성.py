import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    bracket = input()
    stack = []
    for char in bracket:  # bracket의 한 글자씩 순환합니다.
        if not stack or char != stack[-1]: # 만약 스택이 존재하지 않거나 순환하는 글자가 스택의 마지막에 없다면,
            stack.append(char)  # 스택에 글자를 추가 합니다.
        else:
            stack.pop()       # 순환하는 글자가 스택의 마지막에 존재한다면 pop을 통해 제거합니다.

    result = len(stack)   # 반복문자를 지운 스택의 길이를 구해줍니다.
    print(f'#{tc} {result}')
